from cProfile import label

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd import images_path
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText
from kivymd.uix.list import MDList, MDListItem, MDListItemTertiaryText, MDListItemSupportingText, MDListItemLeadingIcon

from KivyMD.kivymd.uix.button import MDButton
from KivyMD.kivymd.uix.dialog import MDDialog, MDDialogContentContainer
from KivyMD.kivymd.uix.label import MDLabel

from KivyMD.kivymd.uix.scrollview import MDScrollView
from aliasmd.aliasmd import farsi
from aliasmd.func import miladi2shamsi_hm

from KivyMD.kivymd.uix.list import MDListItemHeadlineText


class MissionAdd(Screen):
    pass


class aliasButton(Button):
    data = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MoreTable(MDDialogContentContainer):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        src = MDScrollView(do_scroll_x=False)
        src.height = dp(300)
        mdlist = MDList()
        for k, v in data.items():
            mdlist.add_widget(
                MDListItem(
                    MDListItemSupportingText(
                        text=str(k),
                        text_color="black",
                    ),
                )
            )
        src.add_widget(mdlist)
        self.add_widget(src)


class MissionList(Screen):
    def __init__(self, **kwargs):
        super(MissionList, self).__init__(**kwargs)

    def on_enter(self):
        self.loadData_click()

    def gen_label(self, text):
        lbl = Label(
            font_name="ProjectKV/font/iransans.ttf",
            text=farsi(str(text)),
            color="yellow",
            halign="center",
        )
        return lbl

    def gen_more_button(self, text, data):
        mbtn = aliasButton(
            font_name="ProjectKV/font/iransans.ttf",
            text=farsi(str(text)),
            color="yellow",
            halign="center",
        )
        mbtn.data = data
        mbtn.bind(on_release=lambda btn: self.more_info(mbtn))
        return mbtn

    def loadData_click(self):
        app = App.get_running_app()
        misList = app.apis.mession_list_run()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for itm in misList:
            list_view.add_widget(
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="account",
                    ),
                    MDListItemSupportingText(
                        text=miladi2shamsi_hm(itm['rdate'])
                    ),
                    MDListItemTertiaryText(
                        text=itm['title'],
                        text_color="black",
                    ),
                    on_release=lambda itm: self.test(itm),
                ),
            )
        # row.add_widget(self.gen_more_button("بیشتر", itm))
        self.ids['scollable'].add_widget(scroll)

    def test(self, itm):
        print(itm)

    def loadData_click2(self):
        app = App.get_running_app()
        misList = app.apis.mession_list_run()
        rowNo = 1
        for itm in misList:
            row = MDListItem(
                MDLabel(
                    text=miladi2shamsi_hm(itm['rdate']),
                    text_color="black",
                ),
                MDListItemSupportingText(
                    text=str(itm['title']),
                    text_color="black",
                ),
                MDLabel(
                    text=str(rowNo),
                    text_color="black",
                ),
            )
            row.height = dp(30)
            row.add_widget(self.gen_more_button("بیشتر", itm))
            self.ids["box_data"].add_widget(row)
            rowNo += 1

    def more_info(self, instance):
        data = instance.data
        MDDialog(
            MDDialogHeadlineText(
                text="Set backup account",
                halign="left",
            ),
            MoreTable(
                data=data,
                orientation="vertical",
            ),
            orientation="vertical",
        ).open()
