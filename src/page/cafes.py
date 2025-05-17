import flet as ft
from components.galeria_sin_botones import galeria_sin_botones
from components.boton import boton_circular
from components.peticiones import get_all

def cafes_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)
    cafes_inicial = [
        {
            "img": "img/cafes/cafe_pequeño.jpg",
            "title": "Café Americano Pequeño",
            "description": "",
            "price": "Precio 1.00"
        },
        {
            "img": "img/cafes/cafe_grande.jpg",
            "title": "Café Americano Grande",
            "description": "",
            "price": "Precio 1.20"
        },
        {
            "img": "img/cafes/latte.jpeg",
            "title": "Café Latte",
            "description": "",
            "price": "Precio 2.50"
        },
        {
            "img": "img/cafes/capuccino.jpg",
            "title": "Café Capuccino",
            "description": "",
            "price": "Precio 3.00"
        },
        {
            "img": "img/cafes/mocaccino.jpg",
            "title": "Café Moacaccino",
            "description": "",
            "price": "Precio 2.60"
        }
    ]
    
    cafes =  get_all(cafes_inicial,"cafes")
    
    return ft.Column(
        controls=[
            galeria_sin_botones(page,"Cafés", cafes,cambiar_pagina),
        ]
    )
