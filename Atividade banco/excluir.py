from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from editar import * 
from cadastro import *

class Excluir(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)