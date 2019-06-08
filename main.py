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
Config.set('graphics','width',480)
Config.set('graphics','heigth',800)


class caja_1 (BoxLayout):
    def __init__(self, **kwargs):
            super(caja_1, self).__init__()



            self.orientation='vertical'
            caja2=box2()
            caja1= box1()

            self.add_widget(caja2,0)
            self.add_widget(caja1,1)

class box2(BoxLayout):
    pass

    # def on_touch_down(self, touch):
    #     # El toque ha ocurrido dentro del área de widgets. ¡Hacer cosas!
    #     if self.collide_point(*touch.pos):
    #             self.btn.opacity = 0.5
    #
    # def on_touch_up(self, touch):
    #     #para que le evento touch no afecte a los otros  witches
    #     # El toque ha ocurrido dentro del área de widgets. ¡Hacer cosas!
    #     if self.collide_point(*touch.pos):
    #             self.btn.text = 'maik'
    #             self.btn.opacity = 1

class box1(BoxLayout):

    def on_touch_up(self, touch):
        pass



    def  boton(self):
        try:

            if self.label2.text == 'hp':
                dato = float(self.texto.text)
                c = dato / 745.7
                self.etiqueta.text = str("{0:.2f}".format(c))
                self.texto.text = 'input_num'
            else:
                dato = float(self.texto.text)
                c = dato * 745.7
                self.etiqueta.text = str("{0:.2f}".format(c))
                self.texto.text = 'input_num'



        except:
            self.etiqueta.text = 'Error'

    def exchange_text(self):
        texto1= self.label1.text
        texto2 = self.label2.text
        self.label1.text = texto2
        self.label2.text = texto1







    # def on_touch_up(self, touch):
    #     texto= ObjectProperty(None)
    #     #para que le evento touch no afecte a los otros  witches
    #     # El toque ha ocurrido dentro del área de widgets. ¡Hacer cosas!
    #     if self.collide_point(*touch.pos):
    #              self.texto.text= ''




class MainApp(App):
    def build(self):
        return caja_1()


if __name__ == "__main__":
    MainApp().run()
