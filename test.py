import flet as ft

def main(page: ft.Page):
    page.title = "Test"
    page.add(ft.Text("Hello Flet"))

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    port=8080,
)