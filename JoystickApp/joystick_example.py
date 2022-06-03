import pygame
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from pidev.Joystick import Joystick

SCREEN_MANAGER = ScreenManager()
JOYSTICK_SCREEN_NAME = 'main'
SECOND_SCREEN_NAME = 'second'


try:
    joy = Joystick(0, False)
except pygame.error as e:
    print("No joystick connected, please connect and try again.")
    exit(1)


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


class JoystickScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    """

    def __init__(self, **kwargs):
        # this line useful if we want to add attributes but still keep all Screen attributes
        super(JoystickScreen, self).__init__(**kwargs)
        self.joystick_scheduled = False
        # you can make x and y values be instance attributes like this, so they are accessible anywhere in the program
        self.x_val = 0
        self.y_val = 0

    def move_donut(self):
        x_to_add, y_to_add = self.x_val * Window.size[0] * .025, -self.y_val * Window.size[1] * .025
        new_x, new_y = self.ids.donut_btn.center_x + x_to_add, self.ids.donut_btn.center_y + y_to_add
        self.ids.donut_btn.center_x += x_to_add if 0 < new_x < Window.size[0] else 0
        self.ids.donut_btn.center_y += y_to_add if 0 < new_y < Window.size[1] else 0

    def joy_update(self, dt=None):  # dt for clock scheduling
        if SCREEN_MANAGER.current == JOYSTICK_SCREEN_NAME:  # Only update if active screen is joystick screen
            self.x_val, self.y_val = joy.get_both_axes()
            print("Updating Joystick Labels", round(self.x_val, 2), round(self.y_val, 2))
            self.ids.x.text = "X: " + str(round(self.x_val, 2))
            self.ids.y.text = "Y: " + str(round(self.y_val, 2))
            self.move_donut()

        return self.joystick_scheduled  # returning False here would unschedule the Clock from running this function

    def schedule_joy_update(self):
        if not self.joystick_scheduled:  # only schedule once
            Clock.schedule_interval(self.joy_update, .1)  # schedules joy_update to run every .1 seconds
            self.joystick_scheduled = True
            self.ids.schedule_button.text = "Stop Clock"
        else:
            self.joystick_scheduled = False  # joy_update will now return false and thus unschedule the Clock event
            self.ids.schedule_button.text = "Schedule Clock"

    @staticmethod
    def switch_screen():
        SCREEN_MANAGER.transition.direction = "up"
        SCREEN_MANAGER.current = SECOND_SCREEN_NAME


class SecondScreen(Screen):
    @staticmethod
    def switch_screen():
        SCREEN_MANAGER.transition.direction = "down"
        SCREEN_MANAGER.current = JOYSTICK_SCREEN_NAME


"""
Widget additions
"""

Builder.load_file('joystick_example.kv')
SCREEN_MANAGER.add_widget(JoystickScreen(name=JOYSTICK_SCREEN_NAME))
SCREEN_MANAGER.add_widget(SecondScreen(name=SECOND_SCREEN_NAME))


if __name__ == "__main__":
    ProjectNameGUI().run()
