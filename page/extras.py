import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def extras_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    extras = [
        {
            "img": "img/extras/tomates_hilmary.jpg",
            "title": "Tomates Asados",
            "description": "Tomates asados rellenos con puré de papas, queso crema, queso parmesano gratinado y mezclas de finas hierbas deshidratadas.",
            "price": "Precio 4.00"
        },
        {
            "img": "img/extras/papas_fritas.jpg",
            "title": "Papas Fritas",
            "description": "",
            "price": "Precio 2.20"
        },
        {
            "img": "img/extras/ensalada_coleslaw.jpg",
            "title": "Ensalada Cole Slaw",
            "description": "",
            "price": "Precio 1.00"
        },
        {
            "img": "img/extras/extra_morcilla_chorizo.jpg",
            "title": "Ración de Embutidos",
            "description": [
                "Precio US$ 5.00 Extra de Chorizo",
                "Precio US$ 4.00 Extra de Morcilla"
            ],
            "price": "Precio 5.00",
            "lista": True
        },
        {
            "img": "img/extras/papas_rusticas.jpeg",
            "title": "Ración de Papas Rústicas",
            "description": "",
            "price": "Precio 3.20"
        },
        {
            "img": "img/extras/tortillas.jpg",
            "title": "Extra de Tortillas",
            "description": "",
            "price": "Precio 1.60"
        }
    ]

    return ft.Column(
        controls=[
            galeria("Extras",extras),
        ]
    )
