import kivy
kivy.require('1.10.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class HorAlignedBtns(BoxLayout):
    def __init__(self, **kwargs):
        super(HorAlignedBtns, self).__init__(**kwargs)
        self.add_widget(Button(text='Close1'))
        self.add_widget(Button(text='Close2'))
        self.add_widget(Button(text='Close3'))
        self.add_widget(Button(text='Close4'))

class WindowWBtnsAlignedLeftToRight(App):
    def build(self):
        return HorAlignedBtns()

if __name__ == '__main__':
    WindowWBtnsAlignedLeftToRight().run()