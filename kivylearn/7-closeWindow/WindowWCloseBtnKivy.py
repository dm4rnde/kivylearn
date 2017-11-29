import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class WindowWCloseBtn(App):
    def build(self):
        self.btn = Button(text='Close', on_press=self.on_btn_press_event)
        return self.btn

    def on_btn_press_event(self,*args):
        App.get_running_app().stop()
        
if __name__ == '__main__':
    WindowWCloseBtn().run()