from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationrail import MDNavigationRailItem

from master_page import CommonApp


class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_file('dashboard.kv')

    def disabled_widgets(self):
        self.root.ids.rail.disabled = not self.root.ids.rail.disabled


Example().run()
