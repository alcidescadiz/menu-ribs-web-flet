import flet as ft
from components.galeria import galeria
from components.boton import boton_circular

def burger_page(page,cambiar_pagina):
    page.floating_action_button = boton_circular(cambiar_pagina)

    burger = [
        {
            "img": "img/promos/doble_smash.jpg",
            "title": "Burger doble Smash Cheese",
            "description": " Hamburguesa con doble carne de res, doble feta de queso cheddar, pepinillos, salsa espcial de la casa, presentada en un delicioso pan de papa.",
            "price": "Precio 10.50"
        },
        {
            "img": "img/burger/burger_minis.jpg",
            "title": "Tobo Minimini",
            "description": "Diviertete y disfruta con tres mini burger de pollo y tres mini burger de carne, todas con queso cheddar y salsa especial de la casa, acompañado con una guarnición de queso cheddar liquido",
            "price": "Precio 7.00"
        },
        {
            "img": "img/burger/smokedprime.jpg",
            "title": "Smoked Prime",
            "description": "Blend especial de carne de res y cerdo, con queso mozzarella y cheddar derretido, chorizo ahumado, pepinos encurtidos, salsa mayoahumada y chimichurri fresco en pan brioche.",
            "price": "Precio 12.50"
        },
        {
            "img": "img/burger/burger_de_carne.jpg",
            "title": "Burger de Carne",
            "description": "Hamburguesa de carne vacuna al grill en pan de papa, con lechuga, cebolla, tomate y salsa especial Kevin.",
            "price": "Precio 5.50",
            "adicional": True
        },
        {
            "img": "img/burger/burger_de_pollo_crispy.jpg",
            "title": "Chicken Crispy Burger",
            "description": "Pollo empanizado en pan de papa con salsa miel mostaza, lechuga, tomate y cebolla.",
            "price": "Precio 8.50",
            "adicional": True
        },
        {
            "img": "img/burger/burger_de_costilla.jpg",
            "title": "Burger Costilla BBQ",
            "description": "Hamburguesa de costilla de cerdo en pan de papa con salsa BBQ casera, lechuga, tomate y cebolla.",
            "price": "Precio 8.60",
            "adicional": True
        },
        {
            "img": "img/burger/burger_pollo_cesar.jpg",
            "title": "Burger Pollo César",
            "description": "Hamburguesa de pollo con aderezo César casero, lechuga fresca, tocineta crujiente y queso parmesano en pan brioche.",
            "price": "Precio 11.40"
        },
        {
            "img": "img/burger/tnt_burger.jpg",
            "title": "Tnt Burger",
            "description": "Carne de res, tocineta, tomates confitados, queso crema empanizado, salsa de pimentón ahumado.",
            "price": "Precio 9.50"
        },
        {
            "img": "img/burger/burger_ribs.jpg",
            "title": "Rib's Burger",
            "description": "Carne de res y cerdo con salsa BBQ, quesos amarillo, mozzarella y guayanés, aros de cebolla crujientes y tocineta caramelizada en pan brioche.",
            "price": "Precio 12.50"
        },
        {
            "img": "img/burger/burger_ribs_chicken.jpg",
            "title": "Burger Ribs & Chicken Supreme",
            "description": "Carne de cerdo con salsa BBQ, pollo empanizado, quesos amarillo, mozzarella y guayanés, aros de cebolla crujientes y tocineta caramelizada en pan brioche.",
            "price": "Precio 12.50"
        },
        {
            "img": "img/burger/smoked_burger.jpg",
            "title": "Smoked Burger",
            "description": "Carne de res y cerdo ahumada rellena con queso cheddar, cebolla caramelizada en pan de ceniza de berenjena o brioche.",
            "price": "Precio 11.00"
        },
        {
            "img": "img/burger/burger_hillary.jpg",
            "title": "Burger Hillary",
            "description": "Filete de pollo, queso crema empanizado, tocineta, lechuga y salsa César en pan tostado.",
            "price": "Precio 9.30"
        },
        {
            "img": "img/burger/burger_emmy.jpg",
            "title": "Burger Emmy Chicken",
            "description": "La Salsa Emmy, a base de pasta coreana Gochujang, que tiene un picor suave y textura cremosa, acompaña un Pollo empanizado en Doritos, tocineta caramelizada con BBQ, queso cheddar fundido, coleslaw fresco y pepinillos, servido en un pan de berenjena. ",
            "price": "Precio 11.50"
        },
        {
            "img": "img/burger/smoked_italy.jpg",
            "title": "Smoked Italy",
            "description": "Pan de tomate con mayonesa de pesto, rúcula fresca y un ligero toque de vinagreta balsámica. En su interior, un blend de carne y cerdo ahumado con queso Holandés Edam fundido y tomates confitados, combinando matices ahumados, herbales y dulces en cada bocado.",
            "price": "Precio 11.00"
        },
        {
            "img": "img/burger/blue_cheese_burger.png",
            "title": "Blue Cheese Burger",
            "description": "Doble carne de res, salsa de la casa con un toque picante, queso cheddar, pepinillos y una irresistible fusión de cebollas ponchadas con tociteta y queso azul.",
            "price": "Precio 9.90"
        },

    ]
    
    #burger =  get_all(burger_inicial,"burger")

    return ft.Column(
        controls=[
            galeria(page,"Burger",burger,cambiar_pagina)
        ]
    )
