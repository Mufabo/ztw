from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics import Line
from functools import partial
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex

from Data.constants import MAIN_BUTTONS
from Screens.components.Buttons import Btn 

class MenuScreen(Screen):
    def __init__(self, goto, **kwargs):
        super().__init__(**kwargs)

        menuLayout = BoxLayout(orientation="vertical", spacing="20dp")

        for b in MAIN_BUTTONS:
            foo = partial(goto, target=b)
            btn = Btn(text=b,
                      size_hint=(0.5, 1),
                      pos_hint={"center_x": 0.5},
                      color=[0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0],  # goldenrod
                      on_press=foo,
                      )

            menuLayout.add_widget(btn)

        self.add_widget(menuLayout)


