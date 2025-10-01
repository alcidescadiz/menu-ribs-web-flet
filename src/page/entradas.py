import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def entradas_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    entradas = [
        {
            "img": "img/entradas/entrada_minis.jpg",
            "title": "Entrada Mini Minis",
            "description": "Diviertete y disfruta con tres mini burger de pollo y tres mini burger de carne, todas con queso cheddar y salsa especial de la casa, acompañadas de nuestras deliciosas y crujientes papas chesse and bacon.",
            "price": "Precio 13.80"
        },
        {
            "img": "img/entradas/dedos_de_mozzarella.jpg",
            "title": "Dedos de Mozarella",
            "description": "Crujientes palitos de queso mozzarella empanizados y fritos hasta alcanzar un dorado perfecto. Servidos con una deliciosa salsa miel mostaza.",
            "price": "Precio 7.40"
        },
        {
            "img": "img/entradas/papas_cheese_bacon.jpg",
            "title": "Papas Cheese and Bacon",
            "description": "Deliciosas papas fritas, cubiertas con una generosa porción de queso derretido y un toque de polvo de tocineta para realzar su sabor.",
            "price": "Precio 8.10"
        },
        {
            "img": "img/entradas/nachos.jpg",
            "title": "Nachos Falderos",
            "description": "¡Un festín para compartir! Nuestros nachos de maíz, son la base perfecta para una deliciosa combinación con carne de cerdo BBQ, desmenuzada, pico de gallo fresco, queso fundido. Todo ello bañado con una cremosa salsa de aguacate.",
            "price": "Precio 11.70"
        },
        {
            "img": "img/entradas/tequeños.jpg",
            "title": "Tequeños",
            "description": "Tradicionales tequeños rellenos de queso, envueltos en una masa suave y crujiente. Servidos con una salsa miel mostaza que complementa perfectamente su sabor.",
            "price": "Precio 6.10"
        },
        {
            "img": "img/entradas/three_pack.jpg",
            "title": "Three pack",
            "description": "Un plato combinado, con nuestros exquisitos tradicionales tequeños, palitos de queso empanizados y nuestras alitas ahumadas y bañadas en salsa BBQ casera.",
            "price": "Precio 12.80"
        },
        {
            "img": "img/entradas/4x4_tex_mex.jpg",
            "title": "4x4 Tex Mex",
            "description": "Deliciosas quesahots acompañadas de dedos de mozzarella, media ración de nachos, tres golden tenders empanizado con doritos.",
            "price": "Precio 21.50"
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
            "description":"""
            Una fresca mezcla de lechuga romana, crutones dorados, queso parmesano y extra de tocineta, todo bañado en un aderezo César cremoso. 
            Precio US$ 7.40
            Precio US$ 10.30 con extra de pollo
            """,
            "price": "Precio 9.90"
        },
        # {
        #     "img": "img/entradas/ceviche.jpg",
        #     "title": "Ceviche Ribs",
        #     "description": "Pescado marinado en jugo cítrico con toques de ají, cebolla morada y cilantro, acompañada de nuestros crujientes platanitos artesanales dorados a la perfección. Un bocado refrescante, vibrante.",
        #     "price": "Precio 7.80"
        # },
        {
            "img": "img/entradas/ensalada_ribs.jpg",
            "title": "Ensalada Cesar Ribs",
            "description": "Una versión rebelde y sabrosa de la clásica César: crujientes cubos de pork belly y chicharrón botanero coronan una cama de lechuga fresca bañada en aderezo César casero, con un toque generoso de queso pecorino rallado. Una ensalada que no se anda con rodeos, es fresca, intensa y absolutamente irresistible.",
            "price": "Precio 14.20"
        },
        {
            "img": "img/entradas/bunuelos.jpg",
            "title": "Buñuelos",
            "description": "",
            "price": "Precio 5.10"
        },
    ]
    #entradas =  get_all(entradas_inicial,"entradas")
    return ft.Column(
        controls=[
            galeria(page,"Entradas",entradas,cambiar_pagina),
        ]
    )
