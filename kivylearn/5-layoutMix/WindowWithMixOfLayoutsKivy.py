import kivy
from kivy.uix.gridlayout import GridLayout
kivy.require('1.10.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class HorAlignedBtns(BoxLayout):
    def __init__(self, **kwargs):
        super(HorAlignedBtns, self).__init__(**kwargs)
        self.add_widget(Button(text='Close1'))
        self.add_widget(Button(text='Close2'))
        self.add_widget(Button(text='Close3'))
        self.add_widget(Button(text='Close4'))

class VerticalAlignedBtns(GridLayout):
    def __init__(self, **kwargs):
        super(VerticalAlignedBtns, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Button(text='Close1'))
        self.add_widget(Button(text='Close2'))
        self.add_widget(Button(text='Close3'))
        self.add_widget(Button(text='Close4'))

class VerticalAlignedMain(GridLayout):
    def __init__(self, **kwargs):
        super(VerticalAlignedMain, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(HorAlignedBtns())
        self.add_widget(VerticalAlignedBtns())

class WindowWMixedLayouts(App):
    def build(self):
        return VerticalAlignedMain()

if __name__ == '__main__':
    WindowWMixedLayouts().run()