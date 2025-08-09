from kivy.lang import Builder

from kivymd.app import MDApp

from master_page import CommonApp


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_file('nd.kv')

    def disabled_widgets(self):
        pass


Example().run()
