from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from functools import partial
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from Data.constants import *
import plyer
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from Screens.components.Buttons import Btn
from kivy.uix.actionbar import ActionBar, ActionPrevious, ActionView


class MeditationScreen(Screen):
    def __init__(self, goto, **kwargs):
        """
        
        goto: 
        """
        super().__init__(**kwargs)
        self.error = SoundLoader.load('Resources/error.wav')
        self.sound = SoundLoader.load('Resources/tib.wav')

        self.goto = goto
        self.counter = 1

        self.DTN = SETTINGS["dtn"]
        self.time_for_out = SETTINGS["timeOut"]
        self.DURATION = SETTINGS["duration"]
        self.vibrate = SETTINGS["vibration"]

        self.first_side = "right"

        self.next = self.first_side
        self.double_counter = 1

        self.make_layout()

    def inner_timer(self, dt):
        """
        
        """
        if self.time_for_out <= 0:
            print('time out')
            self.counter = 1
            self.time_for_out = int(self.time_for_out)
            self.error.seek(0)
            self.error.play()
            if self.vibrate == "on":
                plyer.vibrator.vibrate(1)
        else:
            self.time_for_out -= 1

    def start_timer(self, btn):
        if btn.text == "start":
            btn.text = "stop"
            self.time_for_out = self.time_for_out  # reset timeout
            print("start timeout")
            self.timeout_clock = Clock.schedule_interval(self.inner_timer, 1)

            self.DURATION = SETTINGS["duration"]
            self.timer.text = "Seconds left: " + str(self.DURATION)
            callback = partial(self.outer_timer, btn=btn)
            self.session_clock = Clock.schedule_interval(callback, 1)
        else:
            # Quit session
            self.next = "right"
            self.timeout_clock.cancel()
            self.session_clock.cancel()
            self.clear_widgets()
            self.DURATION = SETTINGS["duration"]
            self.make_layout()
            self.goto(btn)

    def meditate(self, btn, touch):
        if btn.collide_point(touch.x, touch.y) and self.start.text == "stop":
            if self.counter < self.DTN:
                pos = "left" if touch.spos[0] < 0.5 else "right"
                if pos == self.next:
                    self.next = "left" if self.next == "right" else "right"
                    self.counter += 1
                    print("ok single")
                else:
                    print("sorry single")
                    self.counter = 1
                    self.error.seek(0)
                    self.error.play()
                    if self.vibrate == "on":
                        plyer.vibrator.vibrate(1)
            else:
                pos = "left" if touch.spos[0] < 0.5 else "right"
                if pos == self.next:
                    if self.double_counter % 2 == 0:
                        self.next = "left" if self.next == "right" else "right"
                        self.counter = 1
                        self.double_counter = 1
                        print("double done")
                    else:
                        print("double")
                        self.double_counter += 1
                else:
                    self.counter = 1
                    self.error.seek(0)
                    self.error.play()
                    if self.vibrate == "on":
                        plyer.vibrator.vibrate(1)
                    print("sorry")
        # reset time-out
        self.time_for_out = SETTINGS["timeOut"]

    def outer_timer(self, dt, btn):
        if self.DURATION <= 0:
            # session ends
            self.next = "right"
            self.sound.seek(0)
            self.sound.play()
            self.session_clock.cancel()
            self.timeout_clock.cancel()
            self.timer.text = "Seconds left: " + str(SETTINGS["duration"])
            self.goto(btn)
            return False
        self.DURATION -= 1
        self.timer.text = str(self.DURATION)

    def pause(self, btn):
        if self.start.text == "stop":
            if btn.text == "pause":
                print("pause")
                btn.text = "play"
                self.session_clock.cancel()
                self.timeout_clock.cancel()
            else:
                btn.text = "pause"
                print("play")
                callback = partial(self.outer_timer, btn=btn)
                self.session_clock = Clock.schedule_interval(callback, 1)
                self.timeout_clock = Clock.schedule_interval(
                    self.inner_timer, 1)

    def update(self, key, new_value):
        setattr(self, key, new_value)
        if key == "DURATION":
            self.timer.text = "Seconds left: " + str(self.DURATION)

    def make_layout(self):
        mediLayout = BoxLayout(orientation="vertical")

        back = ActionView()
        back.add_widget(ActionPrevious(
            on_release=self.goto, app_icon='logo.png'))

        self.timer = Label(text="Seconds left: " + str(self.DURATION), color=COLOR_GOLDEN_ROD,)

        self.topRow = BoxLayout(size_hint=(1, 0.1))
        self.topRow.add_widget(back)
        self.topRow.add_widget(self.timer)
        pause_button = Button(on_press=self.pause, text="pause",
                              color=COLOR_GOLDEN_ROD, background_color=[0, 0, 0, 0])
        self.topRow.add_widget(pause_button)

        self.start = Button(text="start", on_press=self.start_timer, background_color=[0, 0, 0, 0],
                            color=COLOR_GOLDEN_ROD,)

        self.topRow.add_widget(self.start)

        mediLayout.add_widget(self.topRow)

        btn = Btn(background_normal="")  # , background_color='#daa520')

        btn.bind(on_touch_down=self.meditate)

        mediLayout.add_widget(btn)
        self.add_widget(mediLayout)
