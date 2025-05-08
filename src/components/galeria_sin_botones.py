import flet as ft
import re


### para galerias de productos q no salen por delivery
### licores,, cocteles

def galeria_sin_botones(page,titulo, lista_productos=[] ):
    if len(lista_productos) < 1:
        return ft.Text(
            f"{titulo} no hay disponibles en este momento",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        )

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
                    ft.Text(lista_producto["price"], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER)

                ]),
                col={"xs": 12, "sm": 10, "md": 6, "lg": 4, "xl": 3},
                border_radius=ft.border_radius.all(8),
                padding=10,
                bgcolor=ft.Colors.BLACK,
                alignment=ft.alignment.center
            )
            for lista_producto in galeria_ordenada
        ]
    )

    return galeria_productos
