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
            "price": "Precio 10.60"
        },
        {
            "img": "./img/platos/alitas_bbq.jpg",
            "title": "Alitas BBQ",
            "description": "Irresistibles alitas BBQ, marinadas y glaseadas con nuestra salsa BBQ casera, que combina dulzura y un toque ahumado, creando una experiencia de sabor inigualable. Servidas con papas fritas crujientes.",
            "price": "Precio 10.80"
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
            "img": "./img/platos/codillo.jpg",
            "title": "Codillo",
            "description": "Sumérgete en una experiencia culinaria única con nuestro Codillo de Cerdo, servido sobre una exquisita reducción de salsa elaborada con piña y especias que aportan un contraste dulce y ácido que realza la riqueza del cerdo. Acompañada con rodajas de piña asada y deliciosa papa gratinada cremosa y dorada al horno.",
            "price": "Precio 20.00"
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
            "price": "Precio 14.00"
        },
        {
            "img": "./img/platos/fiesta-bavara.jpg",
            "title": "Tacos de Fiesta Bavara",
            "description": "La Tabla de Tacos de Fiesta Bávara, es una fusión perfecta entre la tradición alemana y la frescura latina que incluye, tierno y jugoso codillo de cerdo asado, chorizo y chistorra, salsas variadas entre lo dulce y picante, tortillas de trigo ideales para envolver todos los sabores, acompañada con ensalada y papas rústicas.",
            "price": "Precio 36.00"
        },
        {
            "img": "./img/platos/tabla_fiestera.jpg",
            "title": "Tabla Fiestera Maxi",
            "description": "Una combinación de lo más pedido de la casa: suculenta Costilla de Cerdo bañada en salsa BBQ, irresistibles Alitas BBQ y exquisito dorado crocante Pork Belly, acompañados de Papas Cheese.[2 Personas]",
            "price": "Precio 56.80"
        },
        {
          "img":"./img/platos/parrilla_ribs.jpg",
          "title":"Parrilla Ribs",
          "description":"Disfruta de nuestra suculenta parrilla, que combina lo mejor de la tradición con un toque especial. Lomito Grillado, pechuga de pollo, chorizo, morcilla, acompañado de guasacaca, chimichurri. (2 pers)",
          "price":"Precio 31.00"
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
          "price":"Precio 36.00"
        },
        {
            "img": "img/platos/costillas_de_res.jpg",
            "title": "Short Rib",
            "description": "Una majestuosa Costilla de Res glaseada con una profunda y oscura Reducción de demi glace con el toque especial de pipilongo (pimienta larga de origen colombiano), servida con un suave Puré de Papas enriquecido con mantequilla y especias.",
            "price": "Precio 28.00"
        },
        {
            "img": "img/platos/deluxe_de_pollo.jpg",
            "title": "Deluxe de Pollo",
            "description": "Disfruta  de nuestras irresistibles Alitas BBQ y nuestra deliciosa canasta de pollo crujiente, acompañadas de una ración de papas fritas",
            "price": "Precio 11.70"
        },
    ]


    return ft.Column(
        controls=[
            galeria(page,"Platos",platos,cambiar_pagina),
        ]
    )
