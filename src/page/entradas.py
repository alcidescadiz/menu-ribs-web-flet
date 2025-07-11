import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
from components.peticiones import get_all

def entradas_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    entradas_inicial = [
        {
            "img": "img/entradas/entrada_minis.jpg",
            "title": "Entrada Mini Minis",
            "description": "Diviertete y disfruta con tres mini burger de pollo y tres mini burger de carne, todas con queso cheddar y salsa especial de la casa, acompañadas de nuestras deliciosas y crujientes papas chesse and bacon.",
            "price": "Precio 13.29"
        },
        {
            "img": "img/entradas/dedos_de_mozzarella.jpg",
            "title": "Dedos de Mozarella",
            "description": "Crujientes palitos de queso mozzarella empanizados y fritos hasta alcanzar un dorado perfecto. Servidos con una deliciosa salsa miel mostaza.",
            "price": "Precio 6.30"
        },
        {
            "img": "img/entradas/papas_cheese_bacon.jpg",
            "title": "Papas Cheese and Bacon",
            "description": "Deliciosas papas fritas, cubiertas con una generosa porción de queso derretido y un toque de polvo de tocineta para realzar su sabor.",
            "price": "Precio 7.60"
        },
        {
            "img": "img/entradas/nachos.jpg",
            "title": "Nachos Falderos",
            "description": "¡Un festín para compartir! Nuestros nachos de maíz, son la base perfecta para una deliciosa combinación con carne de cerdo BBQ, desmenuzada, pico de gallo fresco, queso fundido. Todo ello bañado con una cremosa salsa de aguacate.",
            "price": "Precio 11.20"
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
            "price": "Precio 12.31"
        },
        {
            "img": "img/entradas/4x4_tex_mex.jpg",
            "title": "4x4 Tex Mex",
            "description": "Deliciosas quesahots acompañadas de dedos de mozzarella, media ración de nachos, tres golden tenders empanizado con doritos.",
            "price": "Precio 18.46"
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
    entradas =  get_all(entradas_inicial,"entradas")
    return ft.Column(
        controls=[
            galeria(page,"Entradas",entradas,cambiar_pagina),
        ]
    )
