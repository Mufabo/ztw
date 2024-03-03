from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.properties import StringProperty, NumericProperty
from Screens.Menu import MenuScreen
# from screens.Meditation import MeditationScreen
# from screens.Donate import DonateScreen
# from screens.Settings import SettingsScreen
# from screens.Statistics import StatisticsScreen
# from screens.About import AboutScreen
from Data.constants import MAIN_BUTTONS
from kivy.core.window import Window


class SM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1,1,1,1)

        #back_to_menu = partial(self.goto, target="menu")

        #global MAIN_BUTTONS
        self.menu = MenuScreen(name="menu", goto= self.goto)
        self.add_widget(self.menu)
        
        #self.meditate = MeditationScreen(back_to_menu, name=MAIN_BUTTONS[0])
        #self.add_widget(self.meditate)
        
        #self.settings = SettingsScreen(back_to_menu,name=MAIN_BUTTONS[1])
        #self.add_widget(self.settings)

        #self.stats = StatisticsScreen(partial(goto, target="menu", sm=self),name=MAIN_BUTTONS[2])
        #self.add_widget(self.stats)

        #self.about = AboutScreen(back_to_menu,name=MAIN_BUTTONS[2])
        #self.add_widget(self.about)

        #self.donate = DonateScreen(partial(goto, target="menu", sm=self),name=MAIN_BUTTONS[4])
        #self.add_widget(self.donate)
        self.current = "menu"

    def goto(self, btn, target):
        if target == "meditate":
            self.meditate.make_layout()
        self.current = target
    
    

sm = SM()


class Ztw(App):
    def build(self):
        self.icon = 'Resources/logo.png'
        return sm


if __name__ == '__main__':
    Ztw().run()
