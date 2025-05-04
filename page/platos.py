import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def platos_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    platos = [
        {
            "img": "img/promos/parrilla_mar_tierra.jpg",
            "title": "Parrilla Mar y Tierra",
            "description": "Una deliciosa combinación de sabores para los amantes de lo mejor de ambos mundos (para dos personas). Jugosos trozos de pollo adobados con condimento parrillero, acompañados de camarones y calamares marinados con ajo y limón. Todo a la parrilla con cebolla, pimentón y mantequilla, servido junto a papas rústicas doradas y una porción de salsa tártara. Una experiencia de sabor única que fusiona tierra y mar.",
            "price": "Precio 24.00"
        },
        {
            "img": "img/platos/canasta_de_pollo.jpg",
            "title": "Canasta de Pollo",
            "description": "Deléitate con nuestra deliciosa canasta de pollo crujiente. Jugosas piezas de pollo empanizadas y fritas hasta alcanzar un dorado perfecto, acompañadas de papas fritas crujientes y salsa miel mostaza.",
            "price": "Precio 9.00"
        },
        {
            "img": "img/platos/alitas_bbq.jpg",
            "title": "Alitas BBQ",
            "description": "Irresistibles alitas BBQ, marinadas y glaseadas con nuestra salsa BBQ casera, que combina dulzura y un toque ahumado. Servidas con papas fritas crujientes.",
            "price": "Precio 9.50"
        },
        {
            "img": "img/platos/alitas_asiaticas.jpg",
            "title": "Alitas Asiáticas",
            "description": "Sumérgete en la fusión de sabores orientales con nuestras exquisitas Alitas Asiáticas, una opción que combina lo mejor de la cocina tradicional con un toque moderno. Se sirven con papas rústicas crujientes.",
            "price": "Precio 9.00"
        },
        {
            "img": "img/platos/alitas_crujientes.jpg",
            "title": "Alitas Crujientes",
            "description": "Alitas de pollo doradas y crujientes, sabrosas y jugosas. Papas fritas doradas, crujientes por fuera y suaves por dentro. Salsa tártara cremosa. Un plato irresistible.",
            "price": "Precio 9.60"
        },
        {
            "img": "img/platos/costillas_bbq.jpg",
            "title": "Costillas BBQ",
            "description": "Una deliciosa y suculenta costilla de cerdo, cocinada a la perfección y bañada en salsa BBQ casera, acompañada de ensalada coleslaw y papas rústicas.",
            "price": "Precio 27.00"
        },
        # Continúa con el resto de los platos...
    ]

    return ft.Column(
        controls=[
            galeria("Platos",platos),
        ]
    )
