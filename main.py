import flet as ft
from page.home import home_page
from page.burger import burger_page
from page.entradas import entradas_page
from page.cafes import cafes_page
from page.cocteles import cocteles_page
from page.extras import extras_page
from page.licores import licores_page
from page.platos import platos_page
from page.postres import postres_page
from page.promociones import promociones_page
from page.bebidas import bebidas_page
from page.carrito import carrito_page
from components.barra_inferior import barra_inferior
from globales.variables_globales import cantidad_carrito


def actualizar_carrito(page, cantidad,cambiar_pagina):
    cantidad_carrito["cantidad"] = cantidad  # ✅ Se actualiza la cantidad total en `main.py`
    page.appbar = crear_barra_superior(page,cambiar_pagina)
    page.update()

# ✅ Función para crear la barra superior dinámicamente
def crear_barra_superior(page,cambiar_pagina):
    def abrir_menu(e):
        page.drawer.open = True
        page.update()

    return ft.AppBar(
        title=ft.Container(
            content=ft.Text("Menú Ribs Burger", font_family="MiFuente", color="white", size=24),
            on_click=lambda e: cambiar_pagina("/home")
        ),
        bgcolor="black",
        center_title=True,
        actions=[
            ft.IconButton(icon=ft.Icons.MENU, on_click=lambda e: abrir_menu(page), icon_color="WHITE"),
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
def main(page: ft.Page):
    global cantidad_carrito

    page.title = "Menu Ribs Burger"
    page.padding = 10
    page.bgcolor = ft.Colors.GREY_600 
    page.fonts = {"MiFuente": "fonts/StyleScript-Regular.ttf"}

    contenido = ft.Container()

    # 🛠 Rutas
    def cambiar_pagina(ruta):
        if ruta == "/home":
            contenido.content = home_page(page)
        elif ruta == "/burger":
            contenido.content = burger_page(page, cambiar_pagina)
        elif ruta == "/entradas":
            contenido.content = entradas_page(page, cambiar_pagina)
        elif ruta == "/cafes":
            contenido.content = cafes_page(page, cambiar_pagina)
        elif ruta == "/cocteles":
            contenido.content = cocteles_page(page, cambiar_pagina)
        elif ruta == "/extras":
            contenido.content = extras_page(page, cambiar_pagina)
        elif ruta == "/licores":
            contenido.content = licores_page(page, cambiar_pagina)
        elif ruta == "/platos":
            contenido.content = platos_page(page, cambiar_pagina)
        elif ruta == "/postres":
            contenido.content = postres_page(page, cambiar_pagina)
        elif ruta == "/promociones":
            contenido.content = promociones_page(page, cambiar_pagina)
        elif ruta == "/bebidas":
            contenido.content = bebidas_page(page, cambiar_pagina)
        elif ruta == "/carrito":
            contenido.content = carrito_page(page, cambiar_pagina)


        page.drawer.open = False
        page.update()

    # 🔹 Vincular `on_route_change` para detectar cambios de ruta
    page.on_route_change = lambda e: cambiar_pagina(e.route)

    # 🔹 Menú lateral
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.ListTile(title=ft.Text("Categorías", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/home")),
            ft.Divider(thickness=2),
            ft.ListTile(title=ft.Text("Burger", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/burger")),
            ft.ListTile(title=ft.Text("Entradas", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/entradas")),
            ft.ListTile(title=ft.Text("Platos", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/platos")),
            ft.ListTile(title=ft.Text("Bebidas", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/bebidas")),
            ft.ListTile(title=ft.Text("Cocteles", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/cocteles")),
            ft.ListTile(title=ft.Text("Postres", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/postres")),
            ft.ListTile(title=ft.Text("Cafés", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/cafes")),
            ft.ListTile(title=ft.Text("Extras", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/extras")),
            ft.ListTile(title=ft.Text("Licores", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/licores")),
            ft.ListTile(title=ft.Text("Promociones", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/promociones")),
            ft.Divider(thickness=2),
            ft.ListTile(title=ft.Text("🛒 Carrito de Compras", font_family="MiFuente", size=24), on_click=lambda e: cambiar_pagina("/carrito"))
        ]
    )

  
    # ✅ Suscribirse a cambios en el carrito
    page.pubsub.subscribe(lambda cantidad: actualizar_carrito(page, cantidad,cambiar_pagina))
    page.appbar = crear_barra_superior(page,cambiar_pagina)
    

    page.scroll = ft.ScrollMode.AUTO
    page.add(
        #barra_superior,
        contenido,
        barra_inferior()
    )

    # 🔹 Vista inicial con tarjetas
    contenido.content = home_page(page)
    page.update()


ft.app(target=main)

# flet build apk --name "com.RibsBurger.miapp" --icon icon.png
# pyinstaller --onefile --windowed --icon=icon.ico --name RibsBurger main.py

# clspython -m http.server --directory build\web









