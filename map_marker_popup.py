from KivyMD.kivymd.uix.dialog import MDDialog, MDDialogIcon, MDDialogHeadlineText, MDDialogContentContainer
from KivyMD.kivymd.uix.list import MDListItem, MDListItemSupportingText


class ServicesMarkerPopup(MDDialog):

    def __init__(self, marker_data):
        super().__init__()
        self.add_widget(MDDialogIcon(icon="refresh"))
        self.add_widget(MDDialogHeadlineText(text="refresh"))


        self.size_hint = [0.9, 0.8]
        keys = ["BID", "Name", "State", "City", "Village", "Phone", "Website", "Instagram", "AccessRoad",
                "TraditionalResidence", "OrganicFood", "IndigenousMusic", "Score", "Update_Time"]

        for i in range(len(keys)):
            key = keys[i]
            value = marker_data[i]
            if value is None:
                value = "-"
            self.add_widget(MDDialogContentContainer(
                MDListItem(
                MDListItemSupportingText(
                    text=key,
                ),
                MDListItemSupportingText(
                    text=value,
                ),
                theme_bg_color="Custom",
                md_bg_color=self.theme_cls.transparentColor,
            ),
            orientation = "vertical",
            ),)
