import flet as ft

def modal_extras (page,agregar_al_carrito,cambiar_pagina):
    extras = [
        {"title": "Aros de Cebolla", "price": "Precio 2.50"},
        {"title": "Papas Fritas", "price": "Precio 2.20"},
        {"title": "Tocineta", "price": "Precio 1.60"},
        {"title": "Queso Guayanés", "price":"Precio 1.50"},
        {"title": "Queso Cheddar", "price":"Precio 1.40"},
        {"title": "Pepinillos", "price": "Precio 1.00"},
        {"title": "Cebolla Caramelizada", "price": "Precio 1.00"},
        {"title": "Chistorra", "price": "Precio 2.50"},
        {"title": "Queso Crema Empanizado", "price": "Precio 1.40"},
        {"title": "Huevo", "price": "Precio 1.00"},
        {"title": "Pollo Crispy", "price": "Precio 3.50"},
        {"title": "Carne", "price": "Precio 2.10"},
        {"title": "Carne de Costilla", "price": "Precio 3.00"}
    ]

    # Crear lista de extras con icono y divisores
    contenido = ft.Column(
    
        controls=[
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.FIBER_MANUAL_RECORD, color=ft.Colors.BLUE, size=12),
                            ft.Column(
                                controls=[
                                    ft.ElevatedButton(
                                        extra["title"], 
                                        width=200,
                                        color=ft.colors.BLACK,
                                        bgcolor=ft.Colors.GREEN_100,
                                        on_click=lambda e,item= extra,: agregar_al_carrito( e,page,{"title": f"Extra de {item['title']}", "price": item["price"]},cambiar_pagina)
                                    ),
                                    ft.Text(f"{extra['price']}", color=ft.Colors.BLACK,size=14),
                                ],
                                spacing=5,  
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                            
                        ],
                        spacing=12,
                    ),
                    ft.Divider()  # Línea divisora entre cada ítem
                ]
            ) for extra in extras
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Habilita el desplazamiento cuando hay mucho contenido
        expand=True
    )

    # Crear el diálogo modal responsive
    modal = ft.AlertDialog(
        content_padding=10,
        title=ft.Text("EXTRAS", size=22, weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK ),
        content=ft.Container(
            content=contenido,
            width=280,  # Establece el ancho del modal
            height=500,  # Define una altura personalizada
            padding=10
        ),
        actions=[ft.TextButton("Cerrar", on_click=lambda e:page.close(modal))],
        bgcolor=ft.Colors.WHITE
    )
    return modal


