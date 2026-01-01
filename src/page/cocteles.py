import flet as ft
from components.galeria_sin_botones import galeria_sin_botones
from components.boton import boton_circular

def cocteles_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    cocteles = [
        {
            "img": "img/cocteles/aperol_frezze.jpg",
            "title": "Aperol Frezze",
            "description": "Coctel a base del licor italiano Aperol, granizado y con un toque de naranja.",
            "price": "Precio 7.00"
        },
        {
            "img": "img/cocteles/blue_ocean.jpg",
            "title": "Blue Ocean",
            "description": "Base de Licor Blue Curacao con Vodka fusionado con gaseosa de limón y zumo de naranja.",
            "price": "Precio 6.00"
        },
        {
            "img": "img/cocteles/daiquiri_parchita.jpg",
            "title": "Daiquiri Parchita",
            "description": "Parchita congelada, ron blanco, extracto de limón y azúcar.",
            "price": "Precio 4.60"
        },
        {
            "img": "img/cocteles/daiquiri_fresa.jpg",
            "title": "Daiquiri Fresa",
            "description": "Fresa congelada, ron blanco, extracto de limón y azúcar.",
            "price": "Precio 5.50"
        },
        {
            "img": "img/cocteles/tinto_de_verano.jpg",
            "title": "Tinto de Verano",
            "description": "Vino tinto, zumo de limón y sprite.",
            "price": "Precio 5.60"
        },
        {
            "img": "img/cocteles/piña_colada.jpg",
            "title": "Piña Colada",
            "description": "Piña congelada, crema de coco y ron de coco.",
            "price": "Precio 5.00"
        },
        {
            "img": "img/cocteles/mojito_parchita.jpg",
            "title": "Mojitos",
            "description": """
                Mojito de Parchita
                Mojito Caribeño
            """,
            "price": "Precio 4.80",
            "lista": True
        },
        {
            "img": "img/cocteles/morrita.jpg",
            "title": "Morrita",
            "description": "",
            "price": "Precio 4.50"
        },
        {
            "img": "img/cocteles/margarita_devil.jpg",
            "title": "Margarita Devil",
            "description": "Coctel a base de tequila y vino tinto.",
            "price": "Precio 4.40"
        },
        {
            "img": "img/cocteles/coctel_grinch.jpg",
            "title": "The Grinch",
            "description": "Una explosión cítrica y vibrante: tequila y triple sec se mezclan con jugo de naranja fresco y un toque de limón. El Blue Curaçao aporta color y profundidad, mientras el borde de Tajín despierta los sentidos con su picante y salino. Refrescante, visualmente atrevido y perfecto para quienes buscan algo diferente.",
            "price": "Precio 4.50"
        }
    ]

    #cocteles =  get_all(cocteles_inicial,"cocteles")

    return ft.Column(
        controls=[
            galeria_sin_botones(page,"Cocteles",cocteles,cambiar_pagina),
        ]
    )
