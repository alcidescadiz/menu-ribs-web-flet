import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
import datetime

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/promo-pollo_deluxe.jpeg",
            "title": "Deluxe de Pollo",
            "description": "De lunes a Miercoles: Disfruta  de nuestras irresistibles Alitas BBQ y nuestra deliciosa canasta de pollo crujiente, acompañadas de una ración de papas fritas y de bebida un vaso de Nestea.",
            "price": "Precio 10.44"
        },
        {
            "img": "img/promos/promo_trikillos.jpeg",
            "title": "Trikillos Tex Mex",
            "description": "De lunes a Miercoles: Deliciosos burritos rellenos de mix de carne & caraota roja, bañados con guacamole, pico de gallo, coronado con un toque de queso cheddar y de bebida un vaso de Nestea..",
            "price": "Precio 10.44"
        },
        {
            "img": "img/promos/promo_chili_con_carne.jpeg",
            "title": "Nachos con Chili y Guacamole",
            "description": "De lunes a Miercoles: Pidelo sin rodeos ni pensarlo: Nuestros nachos de maíz, son la base perfecta para una deliciosa combinación de  mix de carne & caraota roja, pico de gallo fresco, queso fundido. Todo ello bañado con una cremosa salsa guacamole, y de bebida un vaso de Nestea..",
            "price": "Precio 10.44"
        },
        {
            "img": "img/promoS/promo_tnt.jpeg",
            "title": "Tnt Burger",
            "description": "De lunes a Miercoles: Carne de res, tocineta, tomates confitados, queso crema empanizado, salsa de pimentón ahumado, acompañados de nuestras crujientes papas fritas y de bebida un vaso de Nestea.",
            "price": "Precio 10.44"
        },

    ]

    hoy = datetime.date.today().weekday()

    if hoy == 3 or hoy == 4 or hoy == 5 or hoy == 6:
        promociones =[]

    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
