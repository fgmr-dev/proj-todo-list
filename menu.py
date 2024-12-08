# menu.py
import flet as ft
from util.styles import menu_button_style


def create_item(text, icon, value, on_option_click):
    """Function to create menu items"""
    item_menu = ft.Container(
        tooltip=text,
        content=ft.TextButton(
            content=ft.Row(
                [
                    ft.Icon(name=icon),
                ],
            ),
            on_click=on_option_click,
            data=value,
            style=menu_button_style,
        ),
    )

    return item_menu


def create_menu(on_option_click):
    """Function to create menu"""
    menu = ft.Column(
        [
            create_item("Inicio", "home", "home", on_option_click),
            create_item("Miembros", "group", "team", on_option_click),
            create_item("Acerca de", "info", "about", on_option_click),
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=True,
    )

    menu_container = ft.Container(
        content=menu,
        width=200,
        bgcolor="#21272b",  # Aplicar los estilos del menú
        padding=0,  # Reducir el padding
        border=ft.border.all(10, "transparent"),  # Borde transparente
    )

    return menu_container
