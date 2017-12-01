import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class WindowWTxtinput(App):
    def build(self):
        return TextInput(text='Short text')

if __name__ == '__main__':
    WindowWTxtinput().run()