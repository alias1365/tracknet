from kivy.lang import Builder
from kivymd.app import MDApp

from api import api_server
# from searchpopupmenu import SearchPopupMenu
from map_view import ServicesMapView
from top_menu import TopMenu
from mission import MissionAdd, MissionList
from login import Login
# from gpshelper import GpsHelper
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3


class Manager(ScreenManager):
    pass


class Dashboard(Screen):
    pass


class MainApp(MDApp):
    database = None
    cursor = None
    search_pop = None
    manager = None
    apis = None

    def build(self):
        Builder.load_file('ProjectKV/main.kv')
        manager = Manager()
        manager.add_widget(Login(name='Login'))
        manager.add_widget(Dashboard(name='Dashboard'))
        manager.add_widget(MissionAdd(name='MissionAdd'))
        manager.add_widget(MissionList(name='MissionList'))

        self.manager = manager
        return manager

    def on_start(self):
        self.database = sqlite3.connect("db/mydb.db")
        self.cursor = self.database.cursor()
        self.apis = api_server()
        # GpsHelper().run()
        # self.search_pop = SearchPopupMenu()
        # self.theme_cls.primary_palette = "White"


if __name__ == '__main__':
    MainApp().run()
