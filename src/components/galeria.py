import flet as ft
import re
from components.modal_extras import modal_extras
from components.barra_superior import crear_barra_superior
from globales.variables_globales import  carrito, cantidad_carrito
from components.notificaciones import mostrar_notificacion

def agregar_al_carrito(e,page,producto,cambiar_pagina ):
    global cantidad_carrito,carrito
    page.appbar = crear_barra_superior(page,cambiar_pagina)

    # Extraer y convertir precio a float
    title = str(producto["title"])
    price = float(producto["price"][7:]) 
    if title in carrito:
        carrito[title]["cantidad"] += 1  # Aumentar cantidad si ya existe en el carrito
    else:
        carrito[title] = {"price": price, "cantidad": 1}  # Agregar nuevo producto
    
    cantidad_carrito["cantidad"] = sum(item["cantidad"] for item in carrito.values()) 
    mostrar_notificacion(page, f"Agregado {str(producto["title"])} a su pedido",cambiar_pagina)
    page.update()



def galeria(page,titulo, lista_productos,cambiar_pagina ):

    page.appbar = crear_barra_superior(page,cambiar_pagina)

    if len(lista_productos) < 1:
        return ft.Text(
            f"{titulo} no hay disponibles en este momento",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        )

    modal = modal_extras(page,agregar_al_carrito)
    boton_abrir_modal = None
    if titulo == "Burger":
        boton_abrir_modal = ft.ElevatedButton("+1 Extras", on_click=lambda e: page.open(modal))

    def extraer_precio(item):
        return float(item["price"][7:])  # Extraer y convertir precio a float
    
    # Ordenar de mayor a menor
    galeria_ordenada = sorted(lista_productos, key=extraer_precio, reverse=True)
    
    galeria_productos = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Image(src=lista_producto["img"], fit=ft.ImageFit.COVER, width=400),
                    ft.Text(lista_producto["title"], size=24, font_family="MiFuente", color="white", text_align=ft.TextAlign.CENTER),
                    ft.Text(lista_producto["description"], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.JUSTIFY),
                    ft.Text(lista_producto["price"], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                    ft.Column (
                        [ft.Row(
                            
                            controls=[ ft.ElevatedButton(
                            text="Agregar al carrito",
                            on_click=lambda e,item= lista_producto,: agregar_al_carrito( e,page,item,cambiar_pagina),
                            icon=ft.Icons.PLUS_ONE_ROUNDED,
                            bgcolor=ft.Colors.AMBER,
                            color=ft.Colors.BLACK
                            
                            )]+ ([boton_abrir_modal] if boton_abrir_modal else [])
                        )],
                        alignment=ft.alignment.center
                    )

                ],
                alignment=ft.alignment.center),
                col={"xs": 10, "sm": 6, "md": 6, "lg": 4, "xl": 3},
                border_radius=ft.border_radius.all(8),
                padding=10,
                bgcolor=ft.Colors.BLACK
            )
            for lista_producto in galeria_ordenada
        ],
        alignment=ft.alignment.center
    )

    return galeria_productos
