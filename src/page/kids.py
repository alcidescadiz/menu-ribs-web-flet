import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def kids_page(page,cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    kids = [
        {
            "img": "img/kids/combo_1_kids.jpg",
            "title": "Combo Burger Kid",
            "description": """
            
            Disponible solo en local: El Combo Burger Kid tiene un pvp de 11.00 usd.
            """,
            "price": "Precio 11.00"
        },
        {
            "img": "img/kids/combo_kids_3.jpg",
            "title": "Combo Canasta Kid",
            "description": """
            
            Disponible solo en local: El Combo Canasta Kid tiene un pvp de 13.50 usd.
            """,
            "price": "Precio 13.50"
        },
        

    ]
    
    #kids =  get_all(kids_inicial,"kids")

    return ft.Column(
        controls=[
            galeria(page,"Kids",kids,cambiar_pagina)
        ]
    )
