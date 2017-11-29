import kivy
kivy.require('1.10.0')

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class VerticalAlignedBtns(GridLayout):
    def __init__(self, **kwargs):
        super(VerticalAlignedBtns, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Button(text='Close1'))
        self.add_widget(Button(text='Close2'))
        self.add_widget(Button(text='Close3'))
        self.add_widget(Button(text='Close4'))

class WindowWBtnsAlignedTopDown(App):
    def build(self):
        return VerticalAlignedBtns()

if __name__ == '__main__':
    WindowWBtnsAlignedTopDown().run()