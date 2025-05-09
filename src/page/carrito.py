import flet as ft
import urllib.parse
import datetime
from components.boton import boton_circular
from globales.variables_globales import carrito, cantidad_carrito  # ✅ Importamos carrito como diccionario global

# Número de WhatsApp donde se enviará el pedido
numero_whatsapp = "584148757212"

# Función para calcular el total
def calcular_total():
    return sum(datos["cantidad"] * datos["price"] for datos in carrito.values())  # ✅ Iteramos sobre valores del diccionario

# Función para generar el mensaje de WhatsApp con los datos del cliente y la fecha
def generar_mensaje(nombre, telefono, direccion, tipo_pago):
    fecha_pedido = datetime.datetime.now().strftime("%d/%m/%Y")  # Obtiene la fecha actual
    
    mensaje = (
        f"*Pedido de compra*\n"
        f"Fecha: {fecha_pedido}\n"
        f"Cliente: {nombre}\n"
        f"Teléfono: {telefono}\n"
        f"Dirección: {direccion}\n"
        f"Tipo de pago: {tipo_pago}\n\n"
    )
    
    for producto, datos in carrito.items():  # ✅ Iteramos sobre el diccionario
        mensaje += f"- {producto} (x{datos['cantidad']}): ${datos['cantidad'] * datos['price']:.2f}\n"

    mensaje += f"\n*Total a pagar: ${calcular_total():.2f}*\n"
    
    return f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(mensaje)}"  # Enlace con mensaje

def carrito_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    # ✅ Tabla de productos basada en diccionario
    def crear_tabla(carrito):
        return ft.Container(
        content=ft.Row(
            controls=[
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Producto",color="black",weight=ft.FontWeight.BOLD)),
                        ft.DataColumn(ft.Text("Cantidad",color="black",weight=ft.FontWeight.BOLD)),
                        ft.DataColumn(ft.Text("Precio",color="black",weight=ft.FontWeight.BOLD)),
                        ft.DataColumn(ft.Text("Subtotal",color="black",weight=ft.FontWeight.BOLD)),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text(producto,color="black")),  # ✅ Producto es la clave del diccionario
                            ft.DataCell(ft.Text(str(datos["cantidad"]),color="black")),
                            ft.DataCell(ft.Text(f"${datos['price']:.2f}",color="black")),
                            ft.DataCell(ft.Text(f"${datos['cantidad'] * datos['price']:.2f}",color="black")),
                        ],)
                        for producto, datos in carrito.items()  # ✅ Iteramos correctamente sobre el diccionario
                    ],
                ),
            ],
            scroll=ft.ScrollMode.ALWAYS  
        ),
        expand=True  
    )

    tabla = crear_tabla(carrito)

    def actualizar_tabla():
        page.pubsub.send_all({"cantidad": 0, "tipo": "vaciar carrito"}),
        global tabla,total_text 
        contenido.controls[1] = crear_tabla({})
        contenido.controls[2] = ft.Text(f"Total: $0.00", size=20, weight=ft.FontWeight.BOLD,color="black")
        page.update()


    total_text = ft.Text(f"Total: ${calcular_total():.2f}", size=20, weight=ft.FontWeight.BOLD,color="black")


    boton_vaciar_carrito = ft.ElevatedButton(
        text="Borrar pedido",
        on_click=lambda e: [
            actualizar_tabla()
        ],
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.RED,
    )


    # ✅ Botón para enviar pedido con variables correctas
    def enviar_pedido(e):
        nombre = nombre_field.value
        telefono = telefono_field.value
        direccion = direccion_field.value
        tipo_pago = tipo_pago_field.value

        if not nombre or not telefono or not direccion or not tipo_pago:
            # ✅ Mostrar advertencia si faltan datos
            page.open(ft.SnackBar(
                content=ft.Text("⚠️ Por favor completa todos los datos antes de enviar"),
                bgcolor=ft.Colors.RED
            ))
        else:
            page.launch_url(generar_mensaje(nombre, telefono, direccion, tipo_pago))  # ✅ Enviar mensaje con datos correctos
            nombre_field.value=""
            telefono_field.value=""
            direccion_field.value=""
            tipo_pago_field.value=None
            actualizar_tabla()

    # ✅ Campos del formulario
    nombre_field = ft.TextField(label="Nombre y Apellido", width=300)
    telefono_field = ft.TextField(label="Teléfono", width=300)
    direccion_field = ft.TextField(label="Dirección Completa", width=300, multiline=True)
    tipo_pago_field = ft.Dropdown(
        label="Tipo de pago",
        options=[
            ft.dropdown.Option("Efectivo"),
            ft.dropdown.Option("Transferencia"),
            ft.dropdown.Option("Zelle"),
            ft.dropdown.Option("Pago móvil"),
        ],
        width=300
    )

    boton_enviar = ft.ElevatedButton(
        text="Enviar pedido",
        on_click=enviar_pedido,
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.WHITE,
    )

    # ✅ Diseño centrado con formulario
    contenido = ft.Column(
        controls=[
            ft.Text("Carrito de Compras", size=24, weight=ft.FontWeight.BOLD, color="black"),
            tabla,
            total_text,
            boton_vaciar_carrito,
            ft.Text("Datos del Cliente", size=20, weight=ft.FontWeight.BOLD,color="black"),
            nombre_field,
            telefono_field,
            direccion_field,
            tipo_pago_field,
            boton_enviar
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )

    return ft.Container(content=contenido, alignment=ft.alignment.center, padding=20, bgcolor=ft.Colors.WHITE)


