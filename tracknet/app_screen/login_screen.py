import arabic_reshaper
from bidi.algorithm import get_display

from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialogHeadlineText

from .logics.account_class import login
from .logics.dialog_class import msgbox


class loginWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "loginWindow"

    def get_message_text(self, msg):
        if msg == 'label':
            org_text = "بسم"
            reshaped_text = arabic_reshaper.reshape(org_text)
            bidi_text = get_display(reshaped_text)
            return bidi_text
        return "Nothing"

    def login_pressed(self):
        username = self.ids["txt_username"].text
        password = self.ids["txt_password"].text
        lg = login(username, password)
        try:
            authorize = lg.authorization()
        except Exception as e:
            authorize = False
            msgbox(
                icon="close-circle",
                title="Error in login process",
                text=str(e),
            )
        if authorize:
            self.manager.current = 'dashboardWindow'
        else:
            msgbox(
                icon="close-circle",
                title="Authentication Error",
                text="Invalid Username or Password!",
            )
