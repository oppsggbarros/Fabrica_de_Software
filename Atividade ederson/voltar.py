from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager

class MyCadastroMostrar(Screen):
    def __init__(self, **kw):
        super(MyCadastroMostrar, self).__init__(**kw)
        
        self.layout = BoxLayout(orientation = "horizontal")
        self.grid = GridLayout(cols = 2, size_hint = (1, 1))
        
        self.btn_voltar = Button(text="Voltar", size_hint=(1, 0.8))
        self.btn_voltar.bind(on_press=self.cs_voltar)
        
        self.grid.add_widget(self.btn_voltar)
        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)
        
        
    def cs_voltar(self, instance):
        self.manager.current = 'menu'