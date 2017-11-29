import kivy
kivy.require('1.10.0') #change to your kivy version

from kivy.app import App
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class WindowWithLabel(App):
    def build(self):
        return Label(text='Short text')

if __name__ == '__main__':
    WindowWithLabel().run()