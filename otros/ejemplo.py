import flet as ft

def galeria_cafes():
    cafes = [
        {"img": "./img/cafes/cafe_pequeño.jpg", "title": "Café Americano Pequeño", "price": "Precio 1.00"},
        {"img": "./img/cafes/cafe_grande.jpg", "title": "Café Americano Grande", "price": "Precio 1.20"},
        {"img": "./img/cafes/latte.jpeg", "title": "Café Latte", "price": "Precio 2.50"},
        {"img": "./img/cafes/capuccino.jpeg", "title": "Café Capuccino", "price": "Precio 3.00"},
        {"img": "./img/cafes/mocaccino.jpeg", "title": "Café Moacaccino", "price": "Precio 2.60"}
    ]

    # 🔹 Crear una galería responsiva con tarjetas
    galeria = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Image(src=cafe["img"], fit=ft.ImageFit.COVER, width=180, height=160),
                    ft.Text(cafe["title"], size=18, font_family="MiFuente", color="white", text_align=ft.TextAlign.CENTER),
                    ft.Text(cafe["price"], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER)
                ]),
                col={"xs": 6, "sm": 6, "md": 4, "lg": 3, "xl": 3},
                border_radius=ft.border_radius.all(8),
                padding=8,
                bgcolor=ft.Colors.BLACK,
                alignment=ft.alignment.center
            )
            for cafe in cafes
        ]
    )

    return galeria

# 📌 Función principal de la aplicación
def main(page: ft.Page):
    page.title = "Galería de Cafés"
    page.bgcolor = ft.Colors.GREY_800
    page.scroll = ft.ScrollMode.AUTO  # Habilitar scroll si es necesario

    page.add(galeria_cafes())

ft.app(target=main)
