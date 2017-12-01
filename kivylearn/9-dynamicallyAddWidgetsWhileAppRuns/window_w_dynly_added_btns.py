import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class MainContainer(BoxLayout):
    def add_new_btn(self,*args):
        self.add_widget(Button(text='Dynamically added btn'))

class WindowWDynlyAddedBtnsApp(App):        
    def build(self):
        return MainContainer()

if __name__ == '__main__':
    WindowWDynlyAddedBtnsApp().run()