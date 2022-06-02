from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from pidev.kivy import DPEAButton

import cv2

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'
RIGHT_SCREEN_NAME = 'right'
LEFT_SCREEN_NAME = 'left'

VIDEO_PATH = 'ball_bounce_across_stage.mp4'


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


def load_video_from_start():
    return cv2.VideoCapture(VIDEO_PATH)


def convert_to_texture(frame):
    flipped_buf = cv2.flip(frame, 0)
    byte_buf = flipped_buf.tobytes()
    texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    texture.blit_buffer(byte_buf, colorfmt='bgr', bufferfmt='ubyte')
    return texture


class MainScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    """

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.play_video = False
        self.capture = load_video_from_start()
        self.reset_image()  # sets image to start frame
        Clock.schedule_interval(self.update, 1.0 / 33.0)

    def reset_image(self):
        _, frame = self.capture.read()
        texture = convert_to_texture(frame)
        self.ids.img1.texture = texture
        self.play_video = False
        self.ids.start_button.text = 'Start'

    def update(self, dt):
        if self.play_video and SCREEN_MANAGER.current == MAIN_SCREEN_NAME:
            _, frame = self.capture.read()
            if frame is None:
                self.capture = load_video_from_start()
                self.reset_image()
                return
            texture = convert_to_texture(frame)
            self.ids.img1.texture = texture

    def toggle_video(self):
        if self.play_video:
            self.ids.start_button.text = 'Start'
        else:
            self.ids.start_button.text = 'Stop'
        self.play_video = not self.play_video

    @staticmethod
    def switch_to_left():
        SCREEN_MANAGER.transition.direction = "right"
        SCREEN_MANAGER.current = LEFT_SCREEN_NAME

    @staticmethod
    def switch_to_right():
        SCREEN_MANAGER.transition.direction = "left"
        SCREEN_MANAGER.current = RIGHT_SCREEN_NAME


class RightScreen(Screen):
    @staticmethod
    def switch_screen():
        SCREEN_MANAGER.transition.direction = "right"
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME


class LeftScreen(Screen):
    @staticmethod
    def switch_screen():
        SCREEN_MANAGER.transition.direction = "left"
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME


"""
Widget additions
"""

Builder.load_file('VideoApp.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(RightScreen(name=RIGHT_SCREEN_NAME))
SCREEN_MANAGER.add_widget(LeftScreen(name=LEFT_SCREEN_NAME))

if __name__ == "__main__":
    ProjectNameGUI().run()