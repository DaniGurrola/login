import flet as ft

def main(page: ft.Page):
    page.title = "Sistema CETis 61"
    page.window_width = 400
    page.window_height = 500
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    usuario = ft.TextField(
        label="Usuario",
        prefix_icon=ft.Icons.PERSON,
        width=300
    )

    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=300
    )

    mensaje = ft.Text(color="red")

    def login(e):
        if usuario.value == "admin" and contraseña.value == "1234":
            mostrar_panel()
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            page.update()

    boton_login = ft.ElevatedButton(
        "Iniciar sesión",
        icon=ft.Icons.LOGIN,
        on_click=login
    )

    login_view = ft.Column(
        [
            ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=80),
            ft.Text("Inicio de Sesión", size=25, weight="bold"),
            usuario,
            contraseña,
            boton_login,
            mensaje
        ],
        horizontal_alignment="center"
    )

    def mostrar_panel():

        page.controls.clear()

        navbar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME,
                    label="Inicio"
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.EXPLORE,
                    label="Explorar"
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PERSON,
                    label="Perfil"
                ),
            ]
        )

        contenido = ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "Panel Principal",
                        color="white",
                        size=18,
                        weight="bold"
                    ),
                    bgcolor="black",
                    padding=10,
                    width=350
                ),

                ft.Text(
                    "Bienvenido al Sistema",
                    size=25,
                    weight="bold"
                ),

                ft.Text("Has iniciado sesión correctamente"),

                ft.ElevatedButton("Acción")
            ],
            horizontal_alignment="center"
        )

        page.add(contenido)
        page.navigation_bar = navbar
        page.update()

    page.add(login_view)

ft.app(target=main)
