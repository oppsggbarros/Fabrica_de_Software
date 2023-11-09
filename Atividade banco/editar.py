from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from excluir import * 
from cadastro import *

class Editar(Screen):
    def __init__(self, **kwa):
        super().__init__(**kwa)