import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
from components.peticiones import get_all

def kids_page(page,cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    kids = [
        {
            "img": "img/kids/combo_1_kids.jpg",
            "title": "Combo Burger Kid",
            "description": """
            
            Disponible solo en local: El Combo Burger Kid tiene un pvp de 10.50 usd, pero si desea agregarle un helado de paleta el pvp sería de 11.45 usd.
            """,
            "price": "Precio 10.50"
        },
        {
            "img": "img/kids/combo_2_kids.jpg",
            "title": "Combo Minimini kid",
            "description": """
            
            Disponible solo en local: El Combo Minimini Kid tiene un pvp de 10.50 usd, pero si desea agregarle un helado de paleta el pvp sería de 11.45 usd.
            """,
            "price": "Precio 10.50"
        },
        {
            "img": "img/kids/combo_kids_3.jpg",
            "title": "Combo Canasta Kid",
            "description": """
            
            Disponible solo en local: El Combo Canasta Kid tiene un pvp de 13 usd, pero si desea agregarle un helado de paleta el pvp sería de 14 usd.
            """,
            "price": "Precio 13.00"
        },
        

    ]
    
    #kids =  get_all(kids_inicial,"kids")

    return ft.Column(
        controls=[
            galeria(page,"Kids",kids,cambiar_pagina)
        ]
    )
