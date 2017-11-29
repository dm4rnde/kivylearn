import kivy
kivy.require('1.10.0') #change to your kivy version

from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class WindowWithButton(App):
    def build(self):
        return Button(text='Short text')

if __name__ == '__main__':
    WindowWithButton().run()