from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics import Line
from functools import partial
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex


class Btn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color=[0,0,0,0]
        with self.canvas.after:
            Color(218/255, 165/255, 32/255, 1)
            self.line = Line(rectangle=[
                             self.x, self.y, self.width, self.height], width=2)
        self.bind(pos=self.update)
        self.bind(size=self.update)

    def update(self, *args):
        self.line.rectangle = rectangle = [
                             self.x, self.y, self.width, self.height]