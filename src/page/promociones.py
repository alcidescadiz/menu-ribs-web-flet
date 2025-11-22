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
            "price": "Precio 9.00"
        },
        {
            "img": "img/promos/burger_sharing.jpg",
            "title": "Burger Sharing",
            "description": "",
            "price": "Precio 25.00"
        },
        {
            "img": "img/promos/combo_parrillazo.jpg",
            "title": "Combo Parrillazo",
            "description": "",
            "price": "Precio 59.59"
        },
        {
            "img": "img/promos/plato_navidad_promo.jpg",
            "title": "Plato Navidad Ribs",
            "description": "La tradición se sirve con sabor, Hallaca, pan de jamón, ensalada de gallina y nuestro toque especial, Pollo de res ahumado en salsa de carne.",
            "price": "Precio 18.00"
        },

    ]
    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
