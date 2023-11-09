from inicio import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from editar import *
from excluir import * 
from cadastro import *

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicio(name='começo'))
        sm.add_widget(Cadastro(name='cadastro'))
        sm.add_widget(Editar(name='editar'))
        sm.add_widget(Excluir(name='excluir'))
        return sm

if __name__ == '__main__':
    MyApp().run()