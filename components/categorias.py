import flet as ft

def lista_categorias(page: ft.Page):
    categorias_online = [
        {"titulo": "Entradas", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/entradas/4x4_tex_mex.jpg?raw=true", "ruta": "/entradas"},
        {"titulo": "Burger", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/burger/burger_pollo_cesar.jpg?raw=true", "ruta": "/burger"},
        {"titulo": "Platos", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/platos/tabla_fiestera.jpg?raw=true", "ruta": "/platos"},
        {"titulo": "Bebidas", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/bebidas/jugos.png?raw=true", "ruta": "/bebidas"},
        {"titulo": "Cocteles", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/cocteles/Cocteles.png?raw=true", "ruta": "/cocteles"},
        {"titulo": "Postres", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/postres/pie.jpg?raw=true", "ruta": "/postres"},
        {"titulo": "Cafés", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/cafes/capuccino.jpeg?raw=true", "ruta": "/cafes"},
        {"titulo": "Extras", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/extras/tomates_hilmary.jpg?raw=true", "ruta": "/extras"},
        {"titulo": "Licores", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/licores/trago_whisky.jpg?raw=true", "ruta": "/licores"},
        {"titulo": "Promociones", "imagen": "https://github.com/hgrgerencia/menu-ribs/blob/main/img/promos/promos.jpg?raw=true", "ruta": "/promociones"}
    ]
    categorias = [
        {"titulo": "Entradas", "imagen": "img/categorias/ENTRADAS.jpg", "ruta": "/entradas"},
        {"titulo": "Burger", "imagen": "img/categorias/BURGER.jpg", "ruta": "/burger"},
        {"titulo": "Platos", "imagen": "img/categorias/PLATOS.jpg", "ruta": "/platos"},
        {"titulo": "Bebidas", "imagen": "img/categorias/BEBIDAS.jpg", "ruta": "/bebidas"},
        {"titulo": "Cocteles", "imagen": "img/categorias/COCTELES.jpg", "ruta": "/cocteles"},
        {"titulo": "Postres", "imagen": "img/categorias/POSTRES.jpg", "ruta": "/postres"},
        {"titulo": "Cafés", "imagen": "img/categorias/CAFES.jpg", "ruta": "/cafes"},
        {"titulo": "Extras", "imagen": "img/categorias/EXTRAS.jpg", "ruta": "/extras"},
        {"titulo": "Licores", "imagen": "img/categorias/LICORES.jpg", "ruta": "/licores"},
        {"titulo": "Promociones", "imagen": "img/categorias/PROMOS.jpg", "ruta": "/promociones"}
    ]

    def cambiar_vista(ruta):
        page.go(ruta)  # 🔹 Navegar a la nueva vista

    tarjeta_contenedor = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src=categoria["imagen"], fit=ft.ImageFit.COVER, width=220, height=200),
                        ft.Container(
                            content=ft.Text(categoria["titulo"], size=22, font_family="MiFuente", color="white", text_align=ft.TextAlign.CENTER),
                            alignment=ft.alignment.center
                        )
                    ]
                ),
                col={"xs": 6, "sm": 6, "md": 4, "lg": 3, "xl": 3},
                height=260,
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
