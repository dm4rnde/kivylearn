import kivy
kivy.require('1.10.0')

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.graphics import Color

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class HorAlignedElements(BoxLayout):
        
    # important to add - reacts to size changes!
    def _update_lbl1_rect(self, instance, value):
        self.lbl1.rect.pos = instance.pos
        self.lbl1.rect.size = instance.size

    def __init__(self, **kwargs):
        super(HorAlignedElements, self).__init__()
        
        self.lbl1 = Label(text=kwargs['label1_text'])

        with self.lbl1.canvas:
            Color(.2, .7, .3, 0.5)
            self.lbl1.rect = Rectangle(size=self.lbl1.size,
                                   pos=self.lbl1.pos)
        # important to add - reacts to size changes!
        self.lbl1.bind(size=self._update_lbl1_rect, pos=self._update_lbl1_rect)

        self.add_widget(self.lbl1)
        self.add_widget(Label(text=kwargs['label2_text']))

class BgColorAdded2(App):
    def build(self):
        self.title = 'BgColorAdded'
        return HorAlignedElements(label1_text='Text1', label2_text='Text2')

if __name__ == '__main__':
    BgColorAdded2().run()