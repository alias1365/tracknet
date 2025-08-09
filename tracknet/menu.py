import os

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.navigationrail import MDNavigationRailItem

from master_page import CommonApp
from app_screen.login_screen import loginWindow
from app_screen.dashboard_screen import dashboardWindow


class TrackNetApp(MDApp, CommonApp):
    def build(self):
        dir_list = os.listdir('kv_files')
        if len(dir_list) <= 0:
            raise Exception("There is No kv files in the directory!")
        else:
            for kvFile in dir_list:
                Builder.load_file(f"kv_files/{kvFile}")
        screen_manager = ScreenManager()
        screen_manager.add_widget(loginWindow())
        screen_manager.add_widget(dashboardWindow())
        return screen_manager


class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()


if __name__ == '__main__':
    TrackNetApp().run()
