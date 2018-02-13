import kivy
kivy.require('1.10.0')

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.graphics import Color

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class HorAlignedElements1(BoxLayout):
    
    # important to add - reacts to size changes!
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def __init__(self, **kwargs):
        super(HorAlignedElements1, self).__init__()
        
        with self.canvas:
            Color(.3, .4, .8, 0.5)
            self.rect = Rectangle(size=self.size,
                                   pos=self.pos)
        # important to add - reacts to size changes!
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        btn = Button(text=kwargs['btn_txt'])
        lbl = Label(text=kwargs['label_text'])
        self.add_widget(btn)
        self.add_widget(lbl)

class HorAlignedElements2(BoxLayout):
        
    # important to add - reacts to size changes!
    def _update_btn_rect(self, instance, value):
        self.btn.rect.pos = instance.pos
        self.btn.rect.size = instance.size

    # important to add - reacts to size changes!
    def _update_lbl_rect(self, instance, value):
        self.lbl.rect.pos = instance.pos
        self.lbl.rect.size = instance.size

    def __init__(self, **kwargs):
        super(HorAlignedElements2, self).__init__()
        
        self.btn = Button(text=kwargs['btn_txt'])
        
        with self.btn.canvas:
            Color(.4, .0, .0, 0.5)
            self.btn.rect = Rectangle(size=self.btn.size,
                                   pos=self.btn.pos)
        # important to add - reacts to size changes!
        self.btn.bind(size=self._update_btn_rect, pos=self._update_btn_rect)

        self.lbl = Label(text=kwargs['label_text'])

        with self.lbl.canvas:
            Color(.0, .3, .0, 0.5)
            self.lbl.rect = Rectangle(size=self.lbl.size,
                                   pos=self.lbl.pos)
        # important to add - reacts to size changes!
        self.lbl.bind(size=self._update_lbl_rect, pos=self._update_lbl_rect)

        self.add_widget(self.btn)
        self.add_widget(self.lbl)

class VerAlignedElements(BoxLayout):
    def __init__(self, **kwargs):
        super(VerAlignedElements, self).__init__()
        self.orientation = 'vertical'
        self.add_widget(HorAlignedElements1(btn_txt='Close1', label_text='Text1'))
        self.add_widget(HorAlignedElements2(btn_txt='Close2', label_text='Text2'))

class BgColorAdded2(App):
    def build(self):
        self.title = 'BgColorAdded'
        return VerAlignedElements()

if __name__ == '__main__':
    BgColorAdded2().run()