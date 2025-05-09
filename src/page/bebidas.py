import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def bebidas_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    bebidas = [
        {
            "img": "img/bebidas/bebidas.png",
            "title": "Bebidas",
            "description": [
                "4.00 Redbull",
                "3.30 Gatorade",
                "3.20 Refresco 1.5lt (Solo por delivery)",
                "2.70 Soda",
                "2.60 Vaso de Nestea 16oz (Durazno o Limón)",
                "2.50 Agua Minalba 600 ml",
                "2.50 Agua Saborizada",
                "2.50 Refresco de lata",
                "2.20 Vaso de Refresco 16oz (Recargable)",
                "2.20 Jugo Yukery",
                "2.00 Jugo Yuky Pack",
                "1.50 Agua Minalba 355 ml"
            ],
            "price": "Precio 2.60"
        },
        {
            "img": "img/bebidas/jugos.png",
            "title": "Jugos",
            "description": [
                "3.50 Jugo de Fresa",
                "3.50 Jugo de Limón",
                "3.50 Jugo de Parchita",
                "3.50 Jugo de Piña"
            ],
            "price": "Precio 3.50"
        },
        {
            "img": "img/bebidas/berry_bliss.jpg",
            "title": "Berry Bliss",
            "description": "Una bebida vibrante y colorida, perfecta para cualquier ocasión. Rica en vitamina C y antioxidantes, lo que la convierte en una opción saludable. Servido bien frío.",
            "price": "Precio 3.60"
        }
    ]

    return ft.Column(
        controls=[
            galeria(page,"Bebidas", bebidas,cambiar_pagina),
        ],
        alignment=ft.alignment.center
    )
