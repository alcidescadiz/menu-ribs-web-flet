import flet as ft
from components.categorias import lista_categorias


def home_page(page):

    page.floating_action_button = None
    return ft.Column(
        controls=[
            lista_categorias(page)
        ]
    )
