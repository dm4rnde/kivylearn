import kivy
kivy.require('1.10.0')

from kivy.app import App

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class WindowWMixedLayoutsApp(App):
    pass

if __name__ == '__main__':
    WindowWMixedLayoutsApp().run()