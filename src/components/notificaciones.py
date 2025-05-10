import flet as ft
from components.barra_superior import crear_barra_superior

def mostrar_notificacion(page, mensaje,cambiar_pagina):
    page.appbar = crear_barra_superior(page,cambiar_pagina)
    page.open(ft.SnackBar(
        content=ft.Text(mensaje),
        bgcolor=ft.Colors.GREEN
    ))
    page.update()  # ✅ Actualiza la UI
