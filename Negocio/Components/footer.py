import reflex as rx
import datetime
import Negocio.constants as const
from Negocio.Styles.styles import Size, Spacing
from Negocio.Styles.colors import Color, TextColor
# from Negocio.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Castellarin Autorepuestos."
        ),
        rx.link(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.text(
                    "Que lees gil",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v4.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        # Se deja de utilizar hasta que se actualice la versión de next.js
        # float_button(
        #     icon=rx.image(src="/icons/donate.svg"),
        #     href=const.COFFEE_URL
        # ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )