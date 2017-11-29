import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')

class SplittersWidget(BoxLayout):
    pass

class WindowWSplittersApp(App):
    def build(self):
        return SplittersWidget()
    
if __name__ == '__main__':
    WindowWSplittersApp().run()