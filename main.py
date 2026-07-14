import os

import flet as ft
from gspread import Worksheet

class FletDBApp:
    def __init__(self, page: ft.Page):
        self.page = page

        self.setup_page()
        self.create_controls()
        self.buld_ui()

    def setup_page(self):
        self.page.title = "FletDB"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.START

    # -----------------------------
    # コントロール作成
    # -----------------------------
    def create_controls(self):
        print("UI作成")

    # -----------------------------
    # UI
    # -----------------------------
    def buld_ui(self):
        print("UI")

def main(page: ft.Page):
    FletDBApp(page)

ft.app(target=main, port=8080, view="web_browser")