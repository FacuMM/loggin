import flet as ft
import requests

API_URL = "https://loggin-3qu3.onrender.com"  # Cambia esto cuando subas Flask
from init_db import crear_tabla
crear_tabla()

def main(page: ft.Page):
    page.title = "Login App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    username = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True)
    mensaje = ft.Text(value="", color="red")

    def login(e):
        response = requests.post(f"{API_URL}/login", json={"username": username.value, "password": password.value})
        if response.status_code == 200:
            mensaje.value = "¡Login exitoso!"
            mensaje.color = "green"
        else:
            mensaje.value = "Error en login"
            mensaje.color = "red"
        page.update()

    page.add(
        ft.Column(
            controls=[
                username,
                password,
                ft.ElevatedButton("Iniciar sesión", on_click=login),
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
