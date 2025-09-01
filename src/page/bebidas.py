import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def bebidas_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    bebidas = [

        {
            "img": "img/bebidas/jugos.png",
            "title": "Jugos",
            "description": """
            🍓 Jugo de Fresa
            🍋 Jugo de Limón
            🍈 Jugo de Parchita
            🍍 Jugo de Piña
            Jugo de Guanabana
            Jugo de Tamarindo
            """,
            "price": "Precio 3.50",
            "delivery":"False"
        },
        {
            "img": "img/bebidas/berry_bliss.jpg",
            "title": "Berry Bliss",
            "description": "Una bebida vibrante y colorida, perfecta para cualquier ocasión. Rica en vitamina C y antioxidantes, lo que la convierte en una opción saludable. Servido bien frío.",
            "price": "Precio 3.60",
            "delivery":"False"
        },
        {
            "img": "img/bebidas/agua_355.jpg",
            "title": "Agua Minalba 355 ml",
            "description": "",
            "price": "Precio 1.60"
        },
        {
            "img": "img/bebidas/agua_600.jpg",
            "title": "Agua Minalba 600 ml",
            "description": "",
            "price": "Precio 2.50"
        },
        {
            "img": "img/bebidas/agua_saborizada.jpg",
            "title": "Agua Saborizada",
            "description": "",
            "price": "Precio 2.50"
        },
        # gatorade
        {
            "img": "img/bebidas/gatorade.jpg",
            "title": "Gatorade",
            "description": "",
            "price": "Precio 3.80"
        },
        #refresco lata
        {
            "img": "img/bebidas/refresco_lata.jpg",
            "title": "Refresco Lata",
            "description": "",
            "price": "Precio 2.70"
        },
        #refresco 1.5
        {
            "img": "img/bebidas/refresco1.5.jpg",
            "title": "Refresco 1.5lt (Solo por delivery)",
            "description": "",
            "price": "Precio 3.20"
        },
        #refresco 2lt
        {
            "img": "img/bebidas/refresco2.jpg",
            "title": "Refresco 2lt (Solo por delivery)",
            "description": "",
            "price": "Precio 4.00"
        } ,
        # soda
        {
            "img": "img/bebidas/soda.jpg",
            "title": "Soda",
            "description": "",
            "price": "Precio 3.00"
        },
        # yuki pack
        {
            "img": "img/bebidas/yuki_pack.jpg",
            "title": "Jugo Yuky Pack",
            "description": "",
            "price": "Precio 2.20"
        },
        # redbull
        {
            "img": "img/bebidas/redbull.jpg",
            "title": "Redbull",
            "description": "",
            "price": "Precio 4.00"
        },
        {
            "img": "img/bebidas/vaso_nestea.jpg",
            "title": "Vaso de Nestea 16oz (Durazno o Limón)",
            "description": "",
            "price": "Precio 2.60",
            "delivery":"False"
        },
        {
            "img": "img/bebidas/vaso_refresco.jpg",
            "title": "Vaso de Refresco 16oz (Recargable)",
            "description": "",
            "price": "Precio 2.20",
            "delivery":"False"
        },
        {
            "img": "img/bebidas/jugo_yukery.jpg",
            "title": "Jugo Yukery",
            "description": "",
            "price": "Precio 2.20"
        },
        {
            "img": "img/bebidas/malta.jpg",
            "title": "Malta",
            "description": "",
            "price": "Precio 2.10"
        },
        {
            "img": "img/bebidas/te_jamaica.jpg",
            "title": "Té frío de Jamaica",
            "description": "",
            "price": "Precio 2.50",
            "delivery":"False"
        },
    ]
    
    #bebidas =  get_all(bebidas_inicial,"bebidas")
    return ft.Column(
        controls=[
            galeria(page,"Bebidas", bebidas,cambiar_pagina),
        ],
        alignment=ft.alignment.center
    )
