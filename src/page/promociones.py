import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/burger_break.jpg",
            "title": "Burger Break",
            "description": "Suave pan de papa que abraza una jugosa combinación de carne de res y cerdo, coronada con queso cheddar fundido y una mermelada de tocineta que conquista desde el primer bocado. Servida con una ración de papas crujientes para redondear la experiencia.",
            "price": "Precio 10.50"
        },
        {
            "img": "img/promos/burger_sharing.jpg",
            "title": "Burger Sharing",
            "description": "Dos nuevas Burger con blend de carne de res y cerdo y mermelada de tocineta como protagonista, acompañado con una entra con toque mexicano, crujientes Nachos falderos con nuestra carne de costilla especial. Dos mojitos con toque especial de la casa para acompañar la experiencia.",
            "price": "Precio 29.00"
        },
        

    ]
    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
