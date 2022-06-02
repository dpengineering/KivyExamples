from kivy.config import Config  # Keep these Config settings at the top
Config.set('kivy', 'keyboard_mode', 'systemanddock')  # virtual docked keyboard plus input from real keyboard

# simple.json needs to be a file inside of kivy_venv/lib/<python3>/site-packages/kivy/data/keyboards
# for my system, this was '/home/soft-dev/packages/RaspberryPiCommon/kivy_venv/lib/python3.8/site-packages/kivy/data/keyboards'
# Uncomment the following 4 lines to copy simple.json in the appropriate directory--
# import os
# src = '/home/soft-dev/Documents/KivyExamples/OnScreenKeyboardApp/simple.json'
# dest = '/home/soft-dev/packages/RaspberryPiCommon/kivy_venv/lib/python3.8/site-packages/kivy/data/keyboards'
# os.system(f'cp {src} {dest}')
Config.set('kivy', 'keyboard_layout', 'simple')

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

    def reset_text(self):
        self.ids.text_box.text = ''


"""
Widget additions
"""

Builder.load_file('keyboard_example.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

if __name__ == "__main__":
    ProjectNameGUI().run()



