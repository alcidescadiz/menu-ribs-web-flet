import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
import datetime

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
           "img": "img/promos/menu_ejecutivo_navidad.jpg",
           "title": "Menú Ejecutivo Navideño",
           "description": "Disfruta de lunes a jueves nuestra Hallaca artesanal, y a tu elección principal entre nuestro tierno asado negro en su reducción agridulce o el tradicional pernil horneado al punto.",
           "price": "Precio 13.00"
        },
        {
             "img": "img/promos/lunes.jpg",
             "title": "La Tercera es Gratis",
             "description": """Válido lunes y martes """,
             "price": "Precio 00.00"
        },
        # {
        #      "img": "img/promos/mundial.jpg",
        #      "title": "Combo Mundialista",
        #      "description": """
        #     •	UNA (1) RACION DE PAPAS FALDERAS 
        #     •	CUATRO (4) BURGER DOBLE SMASH + 180 GR DE PAPAS FRITAS
        #     •	DOS (2) RAIONES DE ALITAS BBQ (600 GR)
        #     •	DOS RACIONES DE SALSA MIEL MOSTAZA  40 GR
        #     •	CUATRO (4) LATA DE REFRESCO
        #      """,
        #      "price": "Precio 72.00"
        # }

    ]

    #hoy = datetime.date.today().weekday()

    #if hoy == 3 or hoy == 4 or hoy == 5 or hoy == 6:
    #    promociones =[
    #        {
    #            "img": "img/promos/thegoldentable.jpeg",
    #            "title": "Ribs Golden Table",
    #            "description": "Un provocatico mega rack de costilla (aproximadamente 1.6 kg), fajitas, tres de nuestras Burger Premiun, 540 gr de nuestras crujientes papas fritas, una racion de ensalada cesar, acampañada de nuestras mejores salsas. ",
    #            "price": "Precio 120.00"
    #        },
    #    ]

    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
