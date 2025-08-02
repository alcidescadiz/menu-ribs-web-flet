import flet as ft
import importlib
from page.home import home_page
from components.barra_inferior import barra_inferior
from components.barra_superior import crear_barra_superior


def main(page: ft.Page):
    page.title = "Menu Ribs Burger"
    page.padding = 10
    page.bgcolor = ft.Colors.GREY_600
    page.fonts = {"MiFuente": "fonts/StyleScript-Regular.ttf"}
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK

    contenido = ft.Container()

    # 🛠 Rutas
    def cambiar_pagina(ruta):
        page.route = ruta
        modulo = ruta.replace("/", "")
        vista = importlib.import_module(f"page.{modulo}")
        contenido.content = getattr(vista, f"{modulo}_page")(page, cambiar_pagina)
        page.drawer.open = False
        page.update()

    # 🔹 Vincular `on_route_change` para detectar cambios de ruta
    page.on_route_change = lambda e: cambiar_pagina(e.route)

    page.appbar = crear_barra_superior(page, cambiar_pagina)

    # 🔹 Menú lateral
    page.drawer = ft.NavigationDrawer(
        bgcolor=ft.Colors.GREY_100,
        controls=[
            ft.ListTile(
                title=ft.Text("Categorías", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/home"),
            ),
            ft.Divider(thickness=2),
            ft.ListTile(
                title=ft.Text("Burger", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/burger"),
            ),
            ft.ListTile(
                title=ft.Text("Entradas", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/entradas"),
            ),
            ft.ListTile(
                title=ft.Text("Menu Kids", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/kids"),
            ),
            ft.ListTile(
                title=ft.Text("Platos", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/platos"),
            ),
            ft.ListTile(
                title=ft.Text("Bebidas", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/bebidas"),
            ),
            ft.ListTile(
                title=ft.Text("Cocteles", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/cocteles"),
            ),
            ft.ListTile(
                title=ft.Text("Postres", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/postres"),
            ),
            ft.ListTile(
                title=ft.Text("Cafés", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/cafes"),
            ),
            ft.ListTile(
                title=ft.Text("Extras", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/extras"),
            ),
            ft.ListTile(
                title=ft.Text("Licores", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/licores"),
            ),
            ft.ListTile(
                title=ft.Text("Promociones", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/promociones"),
            ),
            ft.Divider(thickness=2),
            ft.ListTile(
                title=ft.Text("🛒 Carrito de Compras", font_family="MiFuente", size=24,color=ft.Colors.BLACK),
                on_click=lambda e: cambiar_pagina("/carrito"),
            ),
        ],
    )

    page.scroll = ft.ScrollMode.AUTO
    page.add(
        # barra_superior,
        contenido,
        barra_inferior(),
    )

    # 🔹 Vista inicial con tarjetas
    contenido.content = home_page(page, cambiar_pagina)
    page.update()


ft.app(target=main)

# web
# 1. python -m http.server --directory build\web
