import flet as ft
from components.categorias import lista_categorias
from components.barra_superior import crear_barra_superior


def home_page(page,cambiar_pagina):
    page.appbar = crear_barra_superior(page,cambiar_pagina)
    page.floating_action_button = None
    return ft.Column(
        controls=[
            lista_categorias(page)
        ]
    )
