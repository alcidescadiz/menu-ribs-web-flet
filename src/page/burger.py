import flet as ft
from components.galeria import galeria
from components.boton import boton_circular
import datetime

def burger_page(page,cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    burger = [
        {
            "img": "img/burger/doble_smash.jpg",
            "title": "Burger doble Smash Cheese",
            "description": " Hamburguesa con doble carne de res, doble feta de queso cheddar, pepinillos, salsa especial de la casa, presentada en un delicioso pan de papa y acompañadas de una ración de papas.",
            "price": "Precio 12.20"
        },
        {
            "img": "img/burger/burger_de_carne.jpg",
            "title": "Burger de Carne",
            "description": "Hamburguesa de carne vacuna al grill en pan de papa, con lechuga, cebolla, tomate y salsa especial Kevin.",
            "price": "Precio 5.80",
            "adicional": True
        },
        {
            "img": "img/burger/burger_de_pollo_crispy.jpg",
            "title": "Chicken Crispy Burger",
            "description": "Pollo empanizado en pan de papa con salsa miel mostaza, lechuga, tomate y cebolla.",
            "price": "Precio 8.60",
            "adicional": True
        },
        {
            "img": "img/burger/burger_pollo_cesar.jpg",
            "title": "Burger Pollo César",
            "description": "Hamburguesa de pollo con aderezo César casero, lechuga fresca, tocineta crujiente y queso parmesano en pan brioche.",
            "price": "Precio 11.70"
        },
        {
            "img": "img/burger/tnt_burger.jpg",
            "title": "Tnt Burger",
            "description": "Carne de res, tocineta, tomates confitados, queso crema empanizado, salsa de pimentón ahumado, acompañada de papas fritas crujientes.",
            "price": "Precio 13.00"
        },
        {
            "img": "img/burger/burger_ribs.jpg",
            "title": "Rib's Burger",
            "description": "Carne de res y cerdo con salsa BBQ, quesos amarillo y mozzarella, aros de cebolla crujientes y tocineta caramelizada en pan brioche.",
            "price": "Precio 13.10"
            ""
        },
        {
            "img": "img/burger/burger_hillary.jpg",
            "title": "Burger Hillary",
            "description": "Filete de pollo empanizado, queso crema empanizado, tocineta, lechuga y salsa César en pan tostado, acompañada de papas fritas crujientes.",
            "price": "Precio 11.20"
        },
        {
            "img": "img/burger/smoked_burger.jpg",
            "title": "Smoked Burger",
            "description": "Blend ahumado (Carne de res y cerdo), feta de queso cheddar, cebolla caramelizada en pan de papa, acompañadas de una ración de papas.",
            "price": "Precio 11.50"
        },
        {
            "img": "img/burger/trioburger.jpg",
            "title": "Medium Trio Burger",
            "description": "Degustación de tres hamburguesas: Res Smashed, Pollo Crispy y Costilla. Incluye tocineta, vegetales, salsas artesanales (Kevin y Mostaza Miel) y un aro de cebolla crujiente. Acompañadas de papas fritas y dip de ketchup. ",
            "price": "Precio 15.10"
        },
        {
            "img": "img/burger/burger_de_costilla.jpg",
            "title": "Burger Costilla BBQ",
            "description": "Hamburguesa de costilla de cerdo en pan de papa con salsa BBQ casera, lechuga, tomate y cebolla.",
            "price": "Precio 8.70",
            "adicional": True
        },
        {
            "img": "img/burger/burger_ribs_chicken.jpg",
            "title": "Burger Ribs & Chicken Supreme",
            "description": "Carne de cerdo con salsa BBQ, pollo empanizado, quesos amarillo y mozzarella, aros de cebolla crujientes y tocineta caramelizada en pan brioche.",
            "price": "Precio 13.10"
        },
        {
            "img": "img/burger/smokedprime.jpg",
            "title": "Smoked Prime",
            "description": "Blend ahumado (Carne de res y cerdo), queso mozzarella y cheddar derretido, chorizo ahumado, pepinos encurtidos, salsa mayoahumada y chimichurri fresco en pan brioche.",
            "price": "Precio 12.50"
        },
        {
            "img": 'img/promos/burger_tributo.jpeg',
            "title": "Burger Tributo",
            "description": "Blend doble al carbón , crema de pecorino y pimienta, tierra de morcilla carupanera , fideos crocantes de tocineta caramelizados en BBQ . Todo eso en pan de chicharrón y Tajín.",
            "price": "Precio 13.00"
        }
    ]

    # viernes_a_domingos = [
        
    # ]
    # hoy = datetime.date.today().weekday()

    # if hoy == 4 or hoy == 5 or hoy == 6:
    #     # burger + viernes_a_domingos
    #     burger = burger + viernes_a_domingos

    return ft.Column(
        controls=[
            galeria(page,"Burger",burger,cambiar_pagina)
        ]
    )
