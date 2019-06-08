#:kivy
 #-*- coding: utf-8 -*-
import kivy
kivy.require('1.10.1')
from kivy.app  import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager,Screen,SwapTransition
from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
Config.set('graphics','width',480)
Config.set('graphics','heigth',800)


class caja_1 (BoxLayout):
    def __init__(self, **kwargs):
            super(caja_1, self).__init__()



            self.orientation='vertical'
            caja1= box1()
            caja2=box2()
            caja3=box3()

            self.add_widget(caja1)
            self.add_widget(caja2)
            self.add_widget(caja3)



class box2(BoxLayout):
#
    pass






    # def on_touch_up(self, touch):
    #     texto= ObjectProperty(None)
    #     #para que le evento touch no afecte a los otros  witches
    #     # El toque ha ocurrido dentro del área de widgets. ¡Hacer cosas!
    #     if self.collide_point(*touch.pos):
    #              self.texto.text= ''
#
# class box3(BoxLayout):
#     pass
#
# class p(Popup):
#     def cambiartext (self):
#
#        box=box2()
#
#        box.label1.text=self.psi.text



class MainApp(App):
    def build(self):
        return caja_1()


if __name__ == "__main__":
    MainApp().run()
