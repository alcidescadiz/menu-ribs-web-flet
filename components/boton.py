import flet as ft

def boton_circular(cambiar_pagina):
    BOTON = ft.FloatingActionButton(
        content=ft.Image(src="img/boton.png", width=50, height=50, fit=ft.ImageFit.COVER),
        bgcolor=ft.Colors.YELLOW,
        shape=ft.RoundedRectangleBorder(radius=28),  # 🔹 Botón circular
        on_click=lambda e: cambiar_pagina("/home")  # Acción de ejemplo
    )
    
    return BOTON




