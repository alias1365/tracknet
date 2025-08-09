from kivymd.uix.appbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App


class TopMenu(MDTopAppBar):
    menu: MDDropdownMenu = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_menu(self, menu_button):
        menu_items = []
        for item, method in {
            "Dashboard": lambda: self.dashboard(),
            "Add New Mission": lambda: self.mission_add(),
            "Your Missions": lambda: self.mission_list(),
        }.items():
            menu_items.append(
                {
                    "text": item,
                    "on_release": method,
                }
            )
        self.menu = MDDropdownMenu(
            caller=menu_button,
            items=menu_items,
        )
        self.menu.open()

    def dashboard(self):
        app = App.get_running_app()
        app.manager.current = "Dashboard"
        self.menu.dismiss()

    def mission_list(self):
        app = App.get_running_app()
        app.manager.current = "MissionList"
        self.menu.dismiss()

    def mission_add(self):
        app = App.get_running_app()
        app.manager.current = "MissionAdd"
        self.menu.dismiss()
