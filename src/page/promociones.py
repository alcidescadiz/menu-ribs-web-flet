import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/burger_break.jpg",
            "title": "Burger Break",
            "description": """Carne de res, tocineta, tomates confitados, queso crema empanizado, salsa de pimentón ahumado, acompañada de crujientes papas fritas y de bebida un vaso de refresco bien frío."
            \nDisponible solo de Lunes a Jueves.""",
            "price": "Precio 8.82"
        },
        {
            "img": "img/promos/burger_sharing.jpg",
            "title": "Burger Sharing",
            "description": "",
            "price": "Precio 24.35"
        },
        {
            "img": "img/promos/burger_tropical.jpg",
            "title": "Burger Tropical Queen",
            "description": "",
            "price": "Precio 8.12"
        },
        

    ]
    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
