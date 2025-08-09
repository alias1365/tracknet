from kivy.app import App
from kivy.uix.screenmanager import Screen



import api
from api import *


class Login(Screen):
    def login_click(self):
        app = App.get_running_app()
        username = self.ids["txt_username"].text
        password = self.ids["txt_password"].text
        self.ids["lbl_msg"].text = "Connecting ..."
        self.ids["btn_login"].disabled = True
        try:
            rs = app.apis.login_run(username, password)
            if rs:
                app.manager.current = "Dashboard"
                self.ids["lbl_msg"].text = ""
            else:
                self.ids["lbl_msg"].text = app.apis.LAST_ERROR
        except Exception as e:
            if str(e).find('Max retries exceeded with')>=0:
                self.ids["lbl_msg"].text = "Network error!"
        self.ids["btn_login"].disabled = False