import flet as ft
from view.home_view import home_view
from view.about_view import about_view
from view.member_view import member_view
from database.manage import fetch_results
from database.schema import create_tables
from database.initial_data import load_data
from content import create_content
from menu import create_menu


def main(page: ft.Page):
    page.title = "Feltra Home :: Tareas"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0

    # Crear sección de contenido
    selected_view = create_content()

    def on_option_click(e):
        if e.control.data == "home":
            selected_view.content = home_view()
        elif e.control.data == "about":
            selected_view.content = about_view()
        elif e.control.data == "team":
            selected_view.content = member_view()
        page.update()

    # Crear sección de menú
    menu_container = create_menu(on_option_click)

    # Cargar secciones en página
    page.add(
        ft.Row(
            [
                menu_container,
                ft.VerticalDivider(width=0, color="transparent"),
                selected_view,
            ],  # Ajustar VerticalDivider
            expand=True,
            spacing=0,
        )
    )

    # Por defecto, mostrar la vista de inicio
    selected_view.content = home_view()
    page.update()


create_tables()
load_data()

ft.app(target=main)
