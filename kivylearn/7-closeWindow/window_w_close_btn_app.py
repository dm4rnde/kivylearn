import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class CloseBtnWidget(BoxLayout):
    #custom widget
    def on_btn_press_event(self,*args):
        App.get_running_app().stop()

class WindowWCloseBtnApp(App):
    def build(self):
        return CloseBtnWidget()
    
if __name__ == '__main__':
    WindowWCloseBtnApp().run()
    