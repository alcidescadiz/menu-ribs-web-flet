import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
import datetime

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/thegoldentable.jpeg",
            "title": "Ribs Golden Table",
            "description": "Un provocatico mega rack de costilla (aproximadamente 1.6 kg), Fajiras, tres de nuestras Burger Premiun, 540 gr de nuestras crujientes papas fritas, una racion de ensalada cesar, acampañada de nuestras mejores salsas. ",
            "price": "Precio 120.00"
        },
        {
             "img": "img/promos/mundial.jpg",
             "title": "COMBO GOLAZO",
             "description": """"
                •	UNA BURGER DOBLE SMASH + 180 GR DE PAPAS
                •	UNA BURGER HILARY + 180 GR PAPAS
                •	UNA (1) ALITAS BBQ (300 GR)
                •	DOS REFRESCO DE LATA
             "",
             "price": "Precio 33.70"
        },
        {
             "img": "img/promos/mundial.jpg",
             "title": "COMBO MUNDIALISTA",
             "description": """"
                •	UNA (1) RACION DE PAPAS FALDERAS 
                    o	360 GR PAPAS CONGELADAS
                    o	80 GRS DE QUESO CHEDDAR LIQUIDO 
                    o	140 GR DE FALDA DE COSTILLA
                    o	RACION DE 40 GR DE PICO DE GALLO
                •	CUATRO (4) BURGER DOBLE SMASH + 180 GR DE PAPAS FRITAS
                •	DOS (2) RAIONES DE ALITAS BBQ (600 GR)
                •	DOS RACIONES DE SALSA MIEL MOSTAZA  40 GR
                •	CUATRO (4) LATA DE REFRESCO
             "",
             "price": "Precio 72.00"
        },
        # {
        #     "img": "img/promos/promo_trikillos.jpeg",
        #     "title": "Trikillos Tex Mex",
        #     "description": "De lunes a Miercoles: Deliciosos burritos rellenos de mix de carne & caraota roja, bañados con guacamole, pico de gallo, coronado con un toque de queso cheddar y de bebida un vaso de Nestea..",
        #     "price": "Precio 10.44"
        # },
        # {
        #     "img": "img/promos/promo_chili_con_carne.jpeg",
        #     "title": "Nachos con Chili y Guacamole",
        #     "description": "De lunes a Miercoles: Pidelo sin rodeos ni pensarlo: Nuestros nachos de maíz, son la base perfecta para una deliciosa combinación de  mix de carne & caraota roja, pico de gallo fresco, queso fundido. Todo ello bañado con una cremosa salsa guacamole, y de bebida un vaso de Nestea..",
        #     "price": "Precio 10.44"
        # },
        # {
        #     "img": "img/promoS/promo_tnt.jpeg",
        #     "title": "Tnt Burger",
        #     "description": "De lunes a Miercoles: Carne de res, tocineta, tomates confitados, queso crema empanizado, salsa de pimentón ahumado, acompañados de nuestras crujientes papas fritas y de bebida un vaso de Nestea.",
        #     "price": "Precio 10.44"
        # },

    ]

    hoy = datetime.date.today().weekday()

    if hoy == 3 or hoy == 4 or hoy == 5 or hoy == 6:
        promociones =[
            {
                "img": "img/promos/thegoldentable.jpeg",
                "title": "Ribs Golden Table",
                "description": "Un provocatico mega rack de costilla (aproximadamente 1.6 kg), fajitas, tres de nuestras Burger Premiun, 540 gr de nuestras crujientes papas fritas, una racion de ensalada cesar, acampañada de nuestras mejores salsas. ",
                "price": "Precio 120.00"
            },
        ]

    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
