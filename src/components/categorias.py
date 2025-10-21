import flet as ft
from components.peticiones import get_all

def lista_categorias(page: ft.Page):
    categorias = [
        {"titulo": "Entradas", "imagen": "img/categorias/ENTRADAS.jpg", "ruta": "/entradas"},
        {"titulo": "Platos", "imagen": "img/categorias/PLATOS.jpg", "ruta": "/platos"},
        {"titulo": "Burger", "imagen": "img/categorias/BURGER.jpg", "ruta": "/burger"},
        {"titulo": "Menú Kids", "imagen": "img/categorias/kids.gif", "ruta": "/kids"},
        {"titulo": "Bebidas", "imagen": "img/categorias/BEBIDAS.jpg", "ruta": "/bebidas"},
        {"titulo": "Cocteles", "imagen": "img/categorias/COCTELES.jpg", "ruta": "/cocteles"},
        {"titulo": "Postres", "imagen": "img/categorias/POSTRES.jpg", "ruta": "/postres"},
        {"titulo": "Cafés", "imagen": "img/categorias/CAFES.jpg", "ruta": "/cafes"},
        {"titulo": "Extras", "imagen": "img/categorias/EXTRAS.jpg", "ruta": "/extras"},
        {"titulo": "Licores", "imagen": "img/categorias/LICORES.jpg", "ruta": "/licores"},
        {"titulo": "Promociones", "imagen": "img/categorias/PROMOS.jpg", "ruta": "/promociones"}
    ]
    #categorias =  get_all(categorias_inicial,"categorias_menu")

    def cambiar_vista(ruta):
        page.go(ruta)  # 🔹 Navegar a la nueva vista

    tarjeta_contenedor = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src=categoria["imagen"], fit=ft.ImageFit.COVER, width=350,height=260 ),
                        ft.Container(
                            content=ft.Text(categoria["titulo"], size=24, font_family="MiFuente", color="white", text_align=ft.TextAlign.CENTER),
                            alignment=ft.alignment.center,
                            
                        )
                    ]
                ),
                col={"xs": 6, "sm": 6, "md": 4, "lg": 3, "xl": 3},
                height=350,
                border_radius=ft.border_radius.all(8),
                padding=8,
                bgcolor=ft.Colors.BLACK,
                alignment=ft.alignment.center,
                on_click=lambda e, ruta=categoria["ruta"]: cambiar_vista(ruta)  # 🔹 Agregar evento de clic
            )
            for categoria in categorias
        ]
    )
    return tarjeta_contenedor
