from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy_garden.mapview import MapMarkerPopup

from KivyMD.kivymd.uix.button import MDButton, MDButtonText
from KivyMD.kivymd.uix.divider import MDDivider
from KivyMD.kivymd.uix.scrollview import MDScrollView
from map_marker_popup import ServicesMarkerPopup
from KivyMD.kivymd.uix.dialog import MDDialog, MDDialogIcon, MDDialogHeadlineText, MDDialogContentContainer, \
    MDDialogSupportingText, MDDialogButtonContainer
from KivyMD.kivymd.uix.list import MDListItem, MDListItemSupportingText, MDListItemLeadingIcon


class map_marker_row(MDListItem):
    def __init__(self, title, value):
        super().__init__()

        self.add_widget(
            MDListItemSupportingText(
                text=f"{title} : {value}",
            ),
            padding=(0, 0),
        )
        self.theme_bg_color = "Custom"


class map_marker_table(MDDialogContentContainer):
    def __init__(self, vList, **kwargs):
        super().__init__(**kwargs)
        # keys = ["BID", "Name", "State", "City", "Village", "Phone", "Website", "Instagram", "AccessRoad",
        #         "TraditionalResidence", "OrganicFood", "IndigenousMusic", "Score", "Update_Time"]
        keys = ["BID", "Name", "State", "City", "Phone"]

        self.add_widget(
            MDDivider(),
        )
        for i in range(len(keys)):
            key = keys[i]
            value = vList[i]
            if value == None:
                value = "-"
            self.add_widget(
                map_marker_row(title=key, value=value),
            )
        self.add_widget(
            MDDivider(),
        )
        self.orientation = "vertical"


class ServicesMarker(MapMarkerPopup):
    marker_data = []
    source = "images/marker.png"
    pop = None

    def on_release(self):
        # pop = ServicesMarkerPopup(self.marker_data)
        pop = MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="refresh",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Reset settings?",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="This will reset your app preferences back to their "
                     "default settings. The following accounts will also "
                     "be signed out:",
            ),
            # -----------------------Custom content------------------------
            map_marker_table(self.marker_data),

            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="close"),
                    style="text",
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
            orientation="vertical",
        )
        pop.open()

    def close(self):
        self.pop.dismiss()
