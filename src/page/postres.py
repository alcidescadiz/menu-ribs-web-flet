import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def postres_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    postres = [
        {
            "img": "img/postres/malteada_brownie.jpg",
            "title": "Malteada de Brownie",
            "description": """
                Helado Cookie and Cream con una porción de brownie
                6.00 Malteada grande 12 onz
                4.00 Malteada pequeña 8 onz
            """,
            "price": "Precio 6.00",
            "delivery":"False"
        },
        {
            "img": "img/postres/malteada_oreo.jpg",
            "title": "Malteada de Oreo",
            "description": """
                Helado de mantecado con galletas oreos.
                5.70 Malteada grande 12 onz
                3.30 Malteada pequeña 8 onz
            """,
            "price": "Precio 5.70",
            "delivery":"False"
        },
        {
            "img": "img/postres/copa_de_helado.jpg",
            "title": "Copa de Helado",
            "description": "Dos porciones de helado cremoso de tu preferencia cubierto con crema chantilly y lluvia.",
            "price": "Precio 4.00",
            "delivery":"False"
        },
        {
            "img": "img/postres/barquillas.jpg",
            "title": "Barquilla o Tinita de dos (2) porciones",
            "description": "Una porción de helado cremoso de tu preferencia con lluvia.",
            "price": "Precio 2.70",
            "delivery":"False"
        },
                {
            "img": "img/postres/barquillas.jpg",
            "title": "Barquilla o Tinita de una (1) porción",
            "description": "Una porción de helado cremoso de tu preferencia con lluvia.",
            "price": "Precio 2.20",
            "delivery":"False"
        },
        {
            "img": "img/postres/malteada.jpg",
            "title": "Malteada",
            "description": "Helado batido decorado con crema chantilly y decorado con lluvia.",
            "price": "Precio 4.00",
            "delivery":"False"
        },
        {
            "img": "img/postres/brownie.jpg",
            "title": "Brownie con Helado",
            "description": "Esponjoso Brownie con una porción de helado cremoso y crema chantilly.",
            "price": "Precio 4.99",
            "delivery":"False"
        },
        {
            "img": "img/postres/quesillo.jpg",
            "title": "Quesillo",
            "description": "Suave quesillo bañado en almíbar.",
            "price": "Precio 4.50"
        },
        {
            "img": "img/postres/pie.jpg",
            "title": "Pie de Limón / Parchita",
            "description": "Pie horneado con una base de galleta y una crema de (Limón / Parchita).",
            "price": "Precio 5.50"
        },
        {
            "img": "img/postres/cheesepie.jpg",
            "title": "Cheese Pie",
            "description": "Cremoso postre frío con una combinación magnífica entre dulce, cítrico y salado.",
            "price": "Precio 6.80"
        },
        {
            "img": "img/postres/cheesecake.jpg",
            "title": "Cheese Cake",
            "description": "Un postre cremoso y decadente, elaborado con queso crema y un toque de vainilla, sobre una base de galleta crujiente.",
            "price": "Precio 7.30"
        },
        {
            "img": "img/postres/galleta_con_helado.jpg",
            "title": "Galleta con Helado",
            "description": "Deliciosa Galleta con una porción de helado cremoso.",
            "price": "Precio 3.60",
            "delivery":"False"
        },
    ]

    return ft.Column(
        controls=[
            galeria(page,"Postres",postres,cambiar_pagina),
        ]
    )
