import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/burger_break.jpg",
            "title": "Burger Break",
            "description": "",
            "price": "Precio 10.50"
        },
        {
            "img": "img/promos/burger_sharing.jpg",
            "title": "Burger Sharing",
            "description": "",
            "price": "Precio 29.00"
        },
        

    ]
    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
