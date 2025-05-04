import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def entradas_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    entradas = [
        {
            "img": "img/entradas/entrada_minis.jpg",
            "title": "Entrada Mini Minis",
            "description": "Disponible de Jueves a Domingo",
            "price": "Precio 12.40"
        },
        {
            "img": "img/entradas/dedos_de_mozzarella.jpg",
            "title": "Dedos de Mozarella",
            "description": "Crujientes palitos de queso mozzarella empanizados y fritos hasta alcanzar un dorado perfecto. Servidos con una deliciosa salsa miel mostaza.",
            "price": "Precio 6.20"
        },
        {
            "img": "img/entradas/papas_cheese_bacon.jpg",
            "title": "Papas Cheese and Bacon",
            "description": "Deliciosas papas fritas, cubiertas con una generosa porción de queso derretido y un toque de polvo de tocineta para realzar su sabor.",
            "price": "Precio 7.50"
        },
        {
            "img": "img/entradas/nachos.jpg",
            "title": "Nachos Falderos",
            "description": "¡Un festín para compartir! Nuestros nachos de maíz, son la base perfecta para una deliciosa combinación con carne de cerdo BBQ, desmenuzada, pico de gallo fresco, queso fundido. Todo ello bañado con una cremosa salsa de aguacate.",
            "price": "Precio 11.00"
        },
        {
            "img": "img/entradas/tequeños.jpg",
            "title": "Tequeños",
            "description": "Tradicionales tequeños rellenos de queso, envueltos en una masa suave y crujiente. Servidos con una salsa miel mostaza que complementa perfectamente su sabor.",
            "price": "Precio 6.00"
        },
        {
            "img": "img/entradas/three_pack.jpg",
            "title": "Three pack",
            "description": "Un plato combinado, con nuestros exquisitos tradicionales tequeños, palitos de queso empanizados y nuestras alitas ahumadas y bañadas en salsa BBQ casera.",
            "price": "Precio 12.00"
        },
        {
            "img": "img/entradas/4x4_tex_mex.jpg",
            "title": "4x4 Tex Mex",
            "description": "Deliciosas quesahots acompañadas de dedos de mozzarella, media ración de nachos, tres golden tenders empanizado con doritos.",
            "price": "Precio 18.00"
        },
        {
            "img": "img/entradas/aros_de_cebolla.jpg",
            "title": "Aros de Cebolla",
            "description": "",
            "price": "Precio 2.50"
        },
        {
            "img": "img/entradas/ensalada_cesar_con_carne.jpg",
            "title": "Ensalada César Clásica",
            "description": [
                "Una fresca mezcla de lechuga romana, crutones dorados, queso parmesano y extra de tocineta, todo bañado en un aderezo César cremoso.",
                "Precio US$ 7.00",
                "Precio US$ 9.90 con extra de pollo"
            ],
            "price": "Precio 9.90",
            "lista": True
        }
    ]

    return ft.Column(
        controls=[
            galeria("Entradas",entradas),
        ]
    )
