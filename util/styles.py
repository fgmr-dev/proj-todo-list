# styles.py
import flet as ft

# Estilo para el texto del menú
menu_text_style = ft.TextStyle(font_family="Segoe UI", color="#859289", size=20)

# Estilo para el fondo de la sección principal
main_section_bg_style = {
    "bgcolor": "#272e33",
}

# Estilo para el texto de la sección principal
main_text_style = ft.TextStyle(font_family="Segoe UI", color="#d3c6aa")

# Estilo para los botones del menú lateral
menu_button_style = ft.ButtonStyle(
    color={"": menu_text_style.color, "hovered": "#d3c6aa"},
    icon_size=30,
    overlay_color={
        "": ft.colors.TRANSPARENT,
        "hovered": ft.colors.TRANSPARENT,
    },  # Para asegurar que no haya superposición de color
)

# Estilo para los botones de la sección principal
main_button_style = ft.ButtonStyle(
    color={"": menu_text_style.color, "hovered": "#d3c6aa"},
    overlay_color={
        "": ft.colors.TRANSPARENT,
        "hovered": ft.colors.TRANSPARENT,
    },  # Para asegurar que no haya superposición de color
)
