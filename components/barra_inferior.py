import flet as ft

def barra_inferior():
    # Barra inferior con texto centrado
    barra_inferior = ft.Container(
        height=80,
        bgcolor="black",
        content=ft.Text(
            value="© 2024 Ribs Burger de Venezuela. Todos los derechos reservados.",
            color="white",
            size=14,
            text_align=ft.TextAlign.CENTER
        ),
        alignment=ft.alignment.center,
    )

    return barra_inferior