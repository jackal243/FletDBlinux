import os

import flet as ft
import pymysql as pms

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

    @staticmethod
    def load_db():
        return pms.connect(
            host="192.168.0.178",
            user="nishi",
            password="tibisennmonn",
            database="fletdb",
            charset="utf8mb4",
            )

    # -----------------------------
    # コントロール作成
    # -----------------------------
    def create_controls(self):
        print("UI作成")
        self.email_area = ft.TextField("Please e-mail")
        self.password_area = ft.TextField("create Pass")
        self.send_button = ft.Button("登録", on_click=self.on_send)

        self.user_email = ft.TextField("Please e-mail")
        self.user_password = ft.TextField("Please password")
        self.user_login = ft.Button("ログイン", on_click=self.on_login)

    # -----------------------------
    # UI
    # -----------------------------
    def buld_ui(self):
        print("UI")

        self.page.add(
            ft.Text("---------------------------------------登録---------------------------------------"),
            ft.Text("E-Mail登録"),
            self.email_area,
            ft.Text("パスワード設定"),
            self.password_area,
            self.send_button,
            ft.Text("---------------------------------------ログイン---------------------------------------"),
            ft.Text("E-Mail"),
            self.user_email,
            ft.Text("パスワード"),
            self.user_password,
            self.user_login
        )
    
    def login(self, email, password):
        conn = self.load_db()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id
                    FROM users
                    WHERE email=%s
                    AND password=%s
                    """,
                    (email, password)
                )

                return cur.fetchone() is not None

        finally:
           print("送信終了")
           conn.close()

    def on_send(self):
        print("送信")
        conn = self.load_db()
        email = self.email_area.value
        password = self.password_area.value
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users(email,password) VALUES(%s,%s)",
                    (email, password)
                    )
                self.conn.commit()
                print("登録完了")
        finally:
            print("登録終了")
            conn.close()
    
    def on_login(self):
        print("ログイン")
        if self.login(self.user_email.value, self.user_password.value):
            self.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("ログイン成功")
                    )
            )
        else:
            self.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("メールアドレスまたはパスワードが違います")
                    )
        )

def main(page: ft.Page):
    FletDBApp(page)

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    port=8080,
)