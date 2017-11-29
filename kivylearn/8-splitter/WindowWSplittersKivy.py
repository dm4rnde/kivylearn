import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.splitter import Splitter

from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')

class WidgAbove(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgAbove, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spl1 = Splitter(sizable_from='bottom', 
                             min_size=80, max_size=220)
        self.spl1.add_widget(Label(text='Closed1'))
        self.add_widget(self.spl1)
        self.add_widget(WidgBelow())
 
class WidgBelow(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgBelow, self).__init__(**kwargs)
        self.spl2 = Splitter(sizable_from='right', 
                             min_size=80, max_size=220)
        self.spl2.add_widget(Label(text='Closed2'))
        self.add_widget(self.spl2)
        self.add_widget(Label(text='Closed3'))
               
class WindowWSplitters(App):
    def build(self):
        return WidgAbove()
    
if __name__ == '__main__':
    WindowWSplitters().run()