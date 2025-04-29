from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from PIL import Image as PILImage

class AnimatedGif(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frames = []
        self.durations = []
        self.frame_index = 0
        self._event = None

        # Start loading gif only if source is already given
        if 'source' in kwargs:
            self.load_gif(self.source)
            self.start_animation()

    def on_source(self, *args):
        # if source is updated later
        self.frames.clear()
        self.durations.clear()
        self.frame_index = 0
        self.load_gif(self.source)
        self.start_animation()

    def load_gif(self, gif_path):
        pil_image = PILImage.open(gif_path)
        try:
            while True:
                frame = pil_image.copy().convert('RGBA')
                texture = self.pil_to_texture(frame)
                self.frames.append(texture)
                duration = pil_image.info.get('duration', 100) / 1000.0
                self.durations.append(duration)
                pil_image.seek(len(self.frames))
        except EOFError:
            pass

    def pil_to_texture(self, pil_image):
        width, height = pil_image.size
        data = pil_image.tobytes()
        texture = Texture.create(size=(width, height))
        texture.blit_buffer(data, colorfmt='rgba', bufferfmt='ubyte')
        texture.flip_vertical()
        return texture

    def start_animation(self):
        if self.frames:
            self._schedule_next_frame()

    def _schedule_next_frame(self, *args):
        if self._event:
            self._event.cancel()
        delay = self.durations[self.frame_index]
        self._event = Clock.schedule_once(self.next_frame, delay)

    def next_frame(self, dt):
        if self.frames:
            self.texture = self.frames[self.frame_index]
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self._schedule_next_frame()
