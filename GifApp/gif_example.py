from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from animatedgif import AnimatedGif

class GifApp(App):
    def build(self):
        Builder.load_file("GifApp/animatedgif.kv")
        return FloatLayout()
    
    def gif_pressed(self):
        print("Gif Button Pressed from App")

if __name__ == "__main__":
    GifApp().run()
