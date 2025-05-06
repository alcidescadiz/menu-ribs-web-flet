import flet as ft
import re
from components.modal_extras import modal_extras
from globales.variables_globales import  carrito, cantidad_carrito


def agregar_al_carrito(e,producto, page):
    # Extraer y convertir precio a float
    title = str(producto["title"])
    price = float(producto["price"][7:]) 
    if title in carrito:
        carrito[title]["cantidad"] += 1  # Aumentar cantidad si ya existe en el carrito
    else:
        carrito[title] = {"price": price, "cantidad": 1}  # Agregar nuevo producto
    
    cantidad_carrito["cantidad"] = sum(item["cantidad"] for item in carrito.values()) 
    page.pubsub.send_all(cantidad_carrito["cantidad"])
    page.update()

    print(cantidad_carrito["cantidad"])


def galeria(page,titulo, lista_productos=[] ):
    if len(lista_productos) < 1:
        return ft.Text(
            f"{titulo} no hay disponibles en este momento",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        )

    modal = modal_extras(page)
    boton_abrir_modal = None
    if titulo == "Burger":
        boton_abrir_modal = ft.ElevatedButton("Agregar Extras", on_click=lambda e: page.open(modal))

    def extraer_precio(item):
        return float(item["price"][7:])  # Extraer y convertir precio a float
    
    # Ordenar de mayor a menor
    galeria_ordenada = sorted(lista_productos, key=extraer_precio, reverse=True)
    
    galeria_productos = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Image(src=lista_producto["img"], fit=ft.ImageFit.FILL, width=350),
                    ft.Text(lista_producto["title"], size=22, font_family="MiFuente", color="white", text_align=ft.TextAlign.CENTER),
                    ft.Text(lista_producto["description"], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.JUSTIFY),
                    ft.Text(lista_producto["price"], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(
                        "Agregar al carrito",
                        on_click=lambda e, item=lista_producto: agregar_al_carrito(e, item, page)  # ✅ Captura cada producto correctamente
                    )

                ] + ([boton_abrir_modal] if boton_abrir_modal else [])),
                col={"xs": 12, "sm": 12, "md": 6, "lg": 4, "xl": 3},
                border_radius=ft.border_radius.all(8),
                padding=8,
                bgcolor=ft.Colors.BLACK,
                alignment=ft.alignment.center
            )
            for lista_producto in galeria_ordenada
        ]
    )

    return galeria_productos
