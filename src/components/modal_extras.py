import flet as ft

def modal_extras (page):
    extras = [
        {"title": "Aros de Cebolla", "price": 2.50},
        {"title": "Papas Fritas", "price": 2.20},
        {"title": "Tocineta", "price": 1.60},
        {"title": "Queso Guayanés", "price": 1.50},
        {"title": "Queso Cheddar", "price": 1.40},
        {"title": "Pepinillos", "price": 1.00},
        {"title": "Cebolla Caramelizada", "price": 1.00},
        {"title": "Chistorra", "price": 2.50},
        {"title": "Queso Crema Empanizado", "price": 1.30},
        {"title": "Huevo", "price": 1.00},
        {"title": "Pollo Crispy", "price": 3.50},
        {"title": "Carne", "price": 2.10},
        {"title": "Carne de Costilla", "price": 3.00}
    ]

    # Crear lista de extras con icono y divisores
    contenido = ft.Column(
    
        controls=[
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.FIBER_MANUAL_RECORD, color=ft.Colors.BLUE, size=12),
                            ft.ElevatedButton(extra["title"], on_click=lambda e: print("agregando extra")),
                            ft.Text(f"${extra['price']}", color=ft.Colors.BLACK,size=14),
                        ],
                        spacing=12
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
        title=ft.Text("EXTRAS", size=22, weight=ft.FontWeight.BOLD),
        content=ft.Container(
            content=contenido,
            width=600,  # Establece el ancho del modal
            height=500,  # Define una altura personalizada
            padding=5
        ),
        actions=[ft.TextButton("Cerrar", on_click=lambda e:page.close(modal))]
    )
    return modal


