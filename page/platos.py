import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def platos_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    platos = [
        {
            "img": "./img/promos/parrilla_mar_tierra.jpg",
            "title": "Parrilla Mar y Tierra",
            "description": """Una deliciosa combinación de sabores para los amantes de lo mejor de ambos mundos (para dos personas).
            Jugosos trozos de pollo adobados con condimento parrillero, acompañados de camarones y calamares marinados con ajo y limón.
            Todo a la parrilla con cebolla, pimentón y mantequilla, servido junto a papas rústicas doradas y una porción de salsa tártara.
            Una experiencia de sabor única que fusiona tierra y mar. 🌊🔥🍗🍤""",
            "price": "Precio 24.00"
        },
        {
            "img": "./img/platos/canasta_de_pollo.jpg",
            "title": "Canasta de Pollo",
            "description": "Deléitate con nuestra deliciosa canasta de pollo crujiente. Este plato consiste en jugosas piezas de pollo empanizadas y fritas hasta alcanzar un dorado perfecto, acompañada de papas fritas crujientes y salsa miel mostaza que elevan la experiencia.",
            "price": "Precio 9.00"
        },
        {
            "img": "./img/platos/alitas_bbq.jpg",
            "title": "Alitas BBQ",
            "description": "Irresistibles alitas BBQ, marinadas y glaseadas con nuestra salsa BBQ casera, que combina dulzura y un toque ahumado, creando una experiencia de sabor inigualable. Servidas con papas fritas crujientes.",
            "price": "Precio 9.50"
        },
        {
            "img": "./img/platos/alitas_asiaticas.jpg",
            "title": "Alitas Asiáticas",
            "description": "Sumérgete en la fusión de sabores orientales con nuestras exquisitas Alitas Asiáticas, una opción que combina lo mejor de la cocina tradicional con un toque moderno, creando un equilibrio perfecto entre lo salado y lo dulce. Se sirven con papas rústicas crujientes.",
            "price": "Precio 9.00"
        },
        {
            "img": "./img/platos/alitas_crujientes.jpg",
            "title": "Alitas Crujientes",
            "description": "Alitas de pollo doradas y crujientes, sabrosas y jugosas. Papas fritas doradas, crujientes por fuera y suaves por dentro. Salsa tártara cremosa, con el equilibrio perfecto de sabores. Un plato irresistible y lleno de sabor. 🍗🍟✨",
            "price": "Precio 9.60"
        },
        {
            "img": "./img/platos/costillas_bbq.jpg",
            "title": "Costillas BBQ",
            "description": "Una deliciosa y suculenta costilla de cerdo, cocinada a la perfección y bañada en una salsa BBQ casera, acompañada de una fresca ensalada coleslaw y crujientes papas rústicas. Este plato es una explosión de sabores que combina lo tierno y ahumado de la carne con la frescura y el crujido de los vegetales.",
            "price": "Precio 27.00"
        },
        {
            "img": "./img/platos/pork_belly.jpg",
            "title": "Pork Belly",
            "description": "Disfruta de una exquisita panceta de cerdo ahumada, cocida a la perfección para lograr una textura crujiente por fuera y tierna por dentro. Este plato se complementa con un fresco pico de gallo, un guacamole cremoso y crujientes papas fritas, creando una experiencia culinaria vibrante y llena de sabor.",
            "price": "Precio 23.00"
        },
        {
            "img": "./img/platos/codillo.jpg",
            "title": "Codillo",
            "description": "Sumérgete en una experiencia culinaria única con nuestro Codillo de Cerdo, servido sobre una exquisita reducción de salsa elaborada con piña y especias que aportan un contraste dulce y ácido que realza la riqueza del cerdo. Acompañada con rodajas de piña asada y deliciosa papa gratinada cremosa y dorada al horno.",
            "price": "Precio 17.00"
        },
        {
            "img": "./img/platos/solomo_grillado.jpg",
            "title": "Lomito Grillado",
            "description": "Jugosa y tierna pieza de carne de lomito, cocinada a la perfección en el grill, servido con un toque de chimichurri, y acompañado con una Ensalada César Clásica, tomates asados rellenos de una mezcla de puré de papas y queso crema coronado con queso parmesano o papa gratinada cremosa al horno.",
            "price": "Precio 16.00"
        },
        {
            "img": "./img/platos/pollo_grillado.jpg",
            "title": "Pollo Grillado",
            "description": "Deléitate con nuestra jugosa pechuga de pollo grillada, marinada a la perfección en hierbas frescas y especias que realzan su sabor. Este plato se sirve con una fresca ensalada César y como acompañamiento, tomates asados rellenos de una mezcla de papas y queso crema o papa gratinada cremosa al horno.",
            "price": "Precio 12.40"
        },
        {
            "img": "./img/platos/fiesta-bavara.jpg",
            "title": "Tacos de Fiesta Bavara",
            "description": "La Tabla de Tacos de Fiesta Bávara, es una fusión perfecta entre la tradición alemana y la frescura latina que incluye, tierno y jugoso codillo de cerdo asado, chorizo y chistorra, salsas variadas entre lo dulce y picante, tortillas de trigo ideales para envolver todos los sabores, acompañada con ensalada y papas rústicas.",
            "price": "Precio 28.80"
        },
        {
            "img": "./img/platos/tabla_fiestera.jpg",
            "title": "Tabla Fiestera",
            "description": "Una combinación de lo más pedido de la casa: suculenta Costilla de Cerdo bañada en salsa BBQ, irresistibles Alitas BBQ y exquisito dorado crocante Pork Belly, acompañados de Papas Cheese y Ensalada Cole Slaw. (3 pers)",
            "price": "Precio 49.80"
        },
        {
            "img": "./img/platos/tabla_fiestera.jpg",
            "title": "Mini Tabla Fiestera",
            "description": "Una combinación de lo más pedido de la casa: suculenta Costilla de Cerdo bañada en salsa BBQ, irresistibles Alitas BBQ y exquisito dorado crocante Pork Belly, acompañados de Papas Cheese y Ensalada Cole Slaw. (2 pers)",
            "price": "Precio 40.00"
        }
    ]


    return ft.Column(
        controls=[
            galeria("Platos",platos),
        ]
    )
