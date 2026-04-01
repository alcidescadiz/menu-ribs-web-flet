import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def platos_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    platos = [
        {
            "img": "./img/platos/canasta_de_pollo.jpg",
            "title": "Canasta de Pollo",
            "description": "Deléitate con nuestra deliciosa canasta de pollo crujiente. Este plato consiste en jugosas piezas de pollo empanizadas y fritas hasta alcanzar un dorado perfecto, acompañada de papas fritas crujientes y salsa miel mostaza que elevan la experiencia.",
            "price": "Precio 10.70"
        },
        {
            "img": "./img/platos/alitas_bbq.jpg",
            "title": "Alitas BBQ",
            "description": "Irresistibles alitas BBQ, marinadas y glaseadas con nuestra salsa BBQ casera, que combina dulzura y un toque ahumado, creando una experiencia de sabor inigualable. Servidas con papas fritas crujientes.",
            "price": "Precio 10.90"
        },
        {
            "img": "./img/platos/costillas_bbq.jpg",
            "title": "Costillas BBQ",
            "description": "Una deliciosa y suculenta costilla de cerdo, cocinada a la perfección y bañada en una salsa BBQ casera, acompañada de una fresca ensalada cesar y crujientes papas rústicas. Este plato es una explosión de sabores que combina lo tierno y ahumado de la carne con la frescura y el crujido de los vegetales.",
            "price": "Precio 28.50"
        },
        {
            "img": "./img/platos/pork_belly.jpg",
            "title": "Pork Belly",
            "description": "Disfruta de una exquisita panceta de cerdo ahumada, cocida a la perfección para lograr una textura crujiente por fuera y tierna por dentro. Este plato se complementa con un fresco pico de gallo, un guacamole cremoso y crujientes papas fritas, creando una experiencia culinaria vibrante y llena de sabor.",
            "price": "Precio 29.70"
        },
        {
            "img": "./img/platos/solomo_grillado.jpg",
            "title": "Lomito Grillado",
            "description": "Jugosa y tierna pieza de carne de lomito, cocinada a la perfección en el grill, servido con un toque de chimichurri, acompañado con una Ensalada César Clásica y papa gratinada cremosa al horno.",
            "price": "Precio 18.00"
        },
        {
            "img": "./img/platos/pollo_grillado.jpg",
            "title": "Pollo Grillado",
            "description": "Deléitate con nuestra jugosa pechuga de pollo grillada, marinada a la perfección en hierbas frescas y especias que realzan su sabor. Este plato se sirve con una fresca ensalada César y como acompañamiento tomate asado relleno de una mezcla de papas.",
            "price": "Precio 14.20"
        },
        {
            "img": "./img/platos/tabla_fiestera.jpg",
            "title": "Tabla Fiestera",
            "description": "Una combinación de lo más pedido de la casa: suculenta Costilla de Cerdo bañada en salsa BBQ, irresistibles Alitas BBQ y exquisito dorado crocante Pork Belly, acompañados de Papas Cheese.[2 Personas]",
            "price": "Precio 56.90"
        },
        {
          "img":"./img/platos/parrilla_ribs.jpg",
          "title":"Parrilla Ribs",
          "description":"Disfruta de nuestra suculenta parrilla, que combina lo mejor de la tradición con un toque especial. Lomito Grillado, pechuga de pollo, chorizo, morcilla, acompañado de guasacaca, chimichurri. (2 pers)",
          "price":"Precio 32.00"
        },
        {
          "img":"./img/platos/fajitas.jpg",
          "title":"Fajitas ",
          "description":"Tiras de filet de pollo y carne de lomito  marinadas en especias y salteadas con pimentones y cebollas en cortes de juliana, acompañados con tortillas de trigo, guacamole, pico de gallo, queso amarillo y salsa tatemada. ",
          "price":"Precio 18.00"
        },
        {
          "img":"./img/platos/parrilla_belly.jpg",
          "title":"Parrilla Belly",
          "description":"Disfruta de nuestra suculenta Parrilla Ribs acompañada coon una panceta de cerdo ahumada, cocida a la perfección para lograr una textura crujiente por fuera y tierna por dentro. ",
          "price":"Precio 36.50"
        },
        {
            "img": "img/platos/deluxe_de_pollo.jpg",
            "title": "Deluxe de Pollo",
            "description": "Disfruta  de nuestras irresistibles Alitas BBQ y nuestra deliciosa canasta de pollo crujiente, acompañadas de una ración de papas fritas",
            "price": "Precio 11.70"
        },
        {
            "img": "img/platos/trikillos.jpg",
            "title": "Trikillos Tex Mex",
            "description": "Deliciosos burritos rellenos de mix de carne & caraota roja, bañados con guacamole, pico de gallo, coronado con un toque de queso cheddar.",
            "price": "Precio 10.00"
        },
        {
            "img": "img/platos/cheddarcorners.jpg",
            "title": "Cheddar Corners",
            "description": "Pidelo sin rodeos ni pensarlo: Nachos con  mix de carne & caraota roja, guacamole, pico de gallo y queso cheddar liquido coronandolos, acompañados de tres tringulos crocantes de queso cheddar rellenos con la combinación perfecta de carne de res y cerdo, y coon nuestra irresistible Salsa Emmy.",
            "price": "Precio 14.99"
        },
    ]


    return ft.Column(
        controls=[
            galeria(page,"Platos",platos,cambiar_pagina),
        ]
    )
