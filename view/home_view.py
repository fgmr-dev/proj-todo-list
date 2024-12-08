# views/home_view.py
import flet as ft
from util.styles import main_text_style


def home_view():
    return ft.Column(
        [
            ft.Text(
                "Bienvenido a la pantalla de inicio!", size=30, style=main_text_style
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )