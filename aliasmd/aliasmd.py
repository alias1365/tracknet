import arabic_reshaper
from bidi.algorithm import get_display
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.core.clipboard import Clipboard, CutBuffer

def farsi(text):
    return get_display(arabic_reshaper.reshape(text))


class MDAliasLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class MDAliasText(MDTextField):
    max_chars = NumericProperty(200)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(MDAliasText, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape(""))

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str + substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(MDAliasText, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str) - 1]
        self.text = get_display(arabic_reshaper.reshape(self.str))

