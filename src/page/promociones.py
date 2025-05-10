import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def promociones_page(page, cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    promociones = [
        {
            "img": "img/promos/parrilla_mar_tierra.jpg",
            "title": "Parrilla Mar y Tierra",
            "description": "Una deliciosa combinación de sabores para los amantes de lo mejor de ambos mundos (para dos personas). Jugosos trozos de pollo adobados con condimento parrillero, acompañados de camarones y calamares marinados con ajo y limón. Todo a la parrilla con cebolla, pimentón y mantequilla, servido junto a papas rústicas doradas y una porción de salsa tártara. Una experiencia de sabor única que fusiona tierra y mar.",
            "price": "Precio 24.00"
        },
        

    ]
    return ft.Column(
        controls=[
            galeria(page,"Promociones",promociones,cambiar_pagina),
        ]
    )
