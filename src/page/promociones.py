import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/doble_smash.jpg",
            "title": "Burger doble Smash Cheese",
            "description": "De Lunes a Jueves de 12:00m a 6:00pm: Hamburguesa con doble carne de res, doble feta de queso cheddar, pepinillos, salsa espcial de la casa, presentada en un delicioso pan de papa.",
            "price": "Precio 5.80"
        },
        

    ]
    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
