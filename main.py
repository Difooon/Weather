import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Погода"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 600


    user_data = ft.TextField(label="Введите город", width=400)
    weather_data = ft.Text("")

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = 'ТОКЕН ИЗ OPENWEATHERMAP'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value = f"Температура: {temp}°C"
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text("Определение погоды"),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row( [ft.ElevatedButton(text="Получить погоду", on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)