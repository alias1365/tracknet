from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

import kivymd

print(kivymd.fonts_path)
class MyKivyMDApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = MDLabel(
            text=u"سلام، این یک متن فارسی در KivyMD است.",
            font_style='Body1',
            halign="center",
            text_size=(300, None),
            text_direction='rtl',
            font_name="/path/to/your/font.ttf"  # مسیر دقیق فونت را جایگزین کنید
        )
        layout.add_widget(label)
        return layout

# MyKivyMDApp().run()
