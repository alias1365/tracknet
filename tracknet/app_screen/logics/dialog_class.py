from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider


class msgbox:
    def create_dialog(self, icon, title, text):
        return MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon=icon,
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text=title,
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text=text,
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),

                MDDivider(),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonIcon(
                        icon="check-circle-outline",
                        theme_icon_color="Custom",
                        icon_color="green",
                        icon_color_disabled="black",
                    ),

                    MDButtonText(
                        text="Accept",
                    ),
                    style="text",
                    on_release=self.close_me(),
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        )

    def __init__(self, icon="refresh", title="this is a confirmation", text="This is a confirmation text message"):
        self.dialog = self.create_dialog(icon=icon, title=title, text=text)
        self.dialog.open()

    def close_me(self):
        print('testtttttt')
        # self.dialog.dismiss()
