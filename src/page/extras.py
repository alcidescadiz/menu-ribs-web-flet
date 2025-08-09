# pylint: disable=import-error
import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
from components.peticiones import get_all

def extras_page(page, cambiar_pagina):
    """vISTA DE EXTRAS"""
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
            "price": "Precio 2.70"
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
            "description":"""
                Precio US$ 5.00 Extra de Chorizo
                Precio US$ 4.20 Extra de Morcilla
            """,
            "price": "Precio 5.00"
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
        },
        {
            "img": "img/extras/extra_bunuelo.jpg",
            "title": "Extra de Buñuelos",
            "description": "",
            "price": "Precio 3.00"
        }
    ]
    
    #extras =  get_all(extras_inicial,"extras")
    return ft.Column(
        controls=[
            galeria(page,"Extras",extras,cambiar_pagina),
        ]
    )
