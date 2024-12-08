import flet as ft


def create_content():
    selected_view = ft.Container(
        expand=True,
        bgcolor="#272e33",
        padding=0,
        border=ft.border.all(0, "transparent"),
    )
    return selected_view
