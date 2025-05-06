import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def licores_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    licores = [
        {
            "img": "img/licores/cerveza_solera.jpg",
            "title": "Cerveza Solera",
            "description": "",
            "price": "Precio 1.80"
        },
        {
            "img": "img/licores/cerveza_pilsen.jpg",
            "title": "Cerveza Pilsen",
            "description": "",
            "price": "Precio 1.60"
        },
        {
            "img": "img/licores/cerveza_caroreña.jpg",
            "title": "Caroreña",
            "description": "",
            "price": "Precio 2.50"
        },
        {
            "img": "img/licores/cerveza_corona.jpg",
            "title": "Cerveza Corona",
            "description": "",
            "price": "Precio 3.00"
        },
        {
            "img": "img/licores/tobo_cerveza_pilsen.jpg",
            "title": "Tobo Cerveza Pilsen (10 und)",
            "description": "",
            "price": "Precio 14.00"
        },
        {
            "img": "img/licores/tobo_cerveza_solera.jpg",
            "title": "Tobo Cerveza Solera (10 und)",
            "description": "",
            "price": "Precio 16.00"
        },
        {
            "img": "img/licores/whisky_12años.jpg",
            "title": "Botella Whisky 12 años",
            "description": "",
            "price": "Precio 50.00"
        },
        {
            "img": "img/licores/cacique_500.jpg",
            "title": "Botella Cacique 500",
            "description": "",
            "price": "Precio 30.00"
        },
        {
            "img": "img/licores/vino_blanco.jpg",
            "title": "Botella de Vino Blanco",
            "description": "",
            "price": "Precio 18.00"
        },
        {
            "img": "img/licores/vino_tinto.jpg",
            "title": "Botella de Vino Tinto",
            "description": "",
            "price": "Precio 18.00"
        },
        {
            "img": "img/licores/trago_ron.jpg",
            "title": "Trago de Ron",
            "description": "",
            "price": "Precio 5.00"
        },
        {
            "img": "img/licores/trago_whisky.jpg",
            "title": "Trago de Whisky",
            "description": "",
            "price": "Precio 5.00"
        },
        {
            "img": "img/licores/copa_de_vino_tinto.jpg",
            "title": "Copa de Vino Tinto",
            "description": "",
            "price": "Precio 4.00"
        },
        {
            "img": "img/licores/copa_de_vino_blanco2.jpg",
            "title": "Copa de Vino Blanco",
            "description": "",
            "price": "Precio 5.00"
        }
    ]

    return ft.Column(
        controls=[
            galeria(page,"Licores",licores),
        ]
    )
