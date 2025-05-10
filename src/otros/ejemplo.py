import flet as ft
import webbrowser  # Para abrir el video en el navegador


def header_image(page):
    """Crea la imagen panorámica"""
    return ft.Container(
        content=ft.Image(src="src/assets/img/platos/fajitas.jpg",
                         fit=ft.ImageFit.COVER),
        width=page.width,
        height=page.height / 2,
    )


def open_video(_):
    """Abre el video de YouTube en el navegador"""
    webbrowser.open("https://www.youtube.com/watch?v=Ffsq8C3Url8")


def youtube_button():
    """Crea un botón que abre el video en YouTube"""
    return ft.Container(
        content=ft.ElevatedButton("Ver Video en YouTube", on_click=open_video),
        padding=ft.padding.all(16),
        expand=True
    )


def mission_vision():
    """Sección de misión y visión"""
    return ft.Container(
        content=ft.Column([
            ft.Text("Nuestra Misión", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Brindar la mejor experiencia gastronómica con hamburguesas, parrillas y ensaladas de la más alta calidad."),
            ft.Text("Nuestra Visión", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Ser el restaurante preferido por los amantes de la buena comida, destacando por nuestro sabor y servicio excepcional."),
        ], spacing=10),
        padding=ft.padding.all(16),
        expand=True
    )


def main(page: ft.Page):
    """Estructura principal de la página"""
    page.title = "Sobre Nosotros"
    page.bgcolor = ft.Colors.WHITE  # Corrección de colors enum
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Crear el layout
    page.add(header_image(page))  # Pasar 'page' a la función
    page.add(ft.Row([youtube_button(), mission_vision()], expand=True))  # Mostrar el botón y la misión/visión

ft.app(target=main)


