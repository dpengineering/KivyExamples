from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from pidev.kivy import DPEAButton

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'
FINISH_SCREEN_NAME = 'finish'


class ProjectNameGUI(App):
    """
    Class to handle running the GUI Application
    """

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        return SCREEN_MANAGER


Window.clearcolor = (1, 1, 1, 1)  # White


class MainScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    """

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.timer_started = False
        self.seconds = self.ids.time_slider.value
        self.time_interval = 1  # second

    def update_count(self, dt):  # dt argument is for Clock Scheduling
        if self.seconds >= 0:
            self.ids.start_button.text = str(self.seconds)
            self.seconds -= self.time_interval
        else:
            self.ids.start_button.text = 'Start Timer'
            self.timer_started = False
            self.switch_to_finish()
            return False  # returning False unschedules the update_count event

    def start_timer(self):
        # There should only ever be a max of 3 clock events, main program, schedule_once, and schedule_interval
        if not self.timer_started and len(Clock.get_events()) <= 3:
            self.timer_started = True
            self.seconds = self.ids.time_slider.value
            Clock.schedule_once(self.update_count)  # to see why this is needed, comment it out and note the delay
            Clock.schedule_interval(self.update_count, self.time_interval)  # update_count runs every time_interval secs

    @staticmethod
    def switch_to_finish():
        SCREEN_MANAGER.transition.direction = "up"
        SCREEN_MANAGER.current = FINISH_SCREEN_NAME


class FinishScreen(Screen):
    @staticmethod
    def switch_screen():
        SCREEN_MANAGER.transition.direction = "down"
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME


"""
Widget additions
"""

Builder.load_file('countdown.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(FinishScreen(name=FINISH_SCREEN_NAME))

if __name__ == "__main__":
    ProjectNameGUI().run()
