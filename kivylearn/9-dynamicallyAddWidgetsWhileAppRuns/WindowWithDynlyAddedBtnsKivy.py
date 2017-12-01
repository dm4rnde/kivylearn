import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class ContainerWVertAlignedContent(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerWVertAlignedContent, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Button(text='Close1'))
        self.add_widget(Button(text='Close2'))
        self.add_widget(Button(text='Add', on_press=self.add_new_btn))
    
    def add_new_btn(self,*args):
        self.add_widget(Button(text='Dynamically added btn'))
        
class WindowWDynlyAddedBtns(App):
    def build(self):
        return ContainerWVertAlignedContent()

if __name__ == '__main__':
    WindowWDynlyAddedBtns().run()