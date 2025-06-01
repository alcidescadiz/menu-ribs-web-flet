import flet as ft
from globales.variables_globales import cantidad_carrito, carrito

def crear_barra_superior(page,cambiar_pagina):
    global cantidad_carrito,carrito
    
    def abrir_menu(e):
        page.drawer.open = True
        page.update()

    return ft.AppBar(
        title=ft.Container(
            content=ft.Text("Menú Ribs Burger", font_family="MiFuente", color=ft.Colors.WHITE, size=24),
            on_click=lambda e: cambiar_pagina("/home")
        ),
        bgcolor=ft.Colors.BLACK,
        center_title=True,
        actions=[
            ft.IconButton(icon=ft.Icons.MENU, on_click=lambda e: abrir_menu(page), icon_color=ft.Colors.WHITE),
            ft.Stack(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.SHOPPING_CART, 
                        on_click=lambda e: cambiar_pagina("/carrito"),
                        padding=10,
                        visible=cantidad_carrito["cantidad"] > 0
                    ),
                    ft.Container(
                        content=ft.Text(str(cantidad_carrito["cantidad"]), size=10, color="white"),
                        bgcolor="red",
                        border_radius=5,
                        padding=5,
                        visible= cantidad_carrito["cantidad"] > 0  # ✅ Se actualiza dinámicamente
                    )
                ]
            )
        ]
    )
