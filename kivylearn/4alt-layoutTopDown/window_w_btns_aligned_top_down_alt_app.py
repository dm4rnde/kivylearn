#alternative top-down layout example
import kivy
kivy.require('1.10.0')

from kivy.app import App

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')

class WindowWBtnsAlignedTopDownAltApp(App):
    pass

if __name__ == '__main__':
    WindowWBtnsAlignedTopDownAltApp().run()