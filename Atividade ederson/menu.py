from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager

class MyCadastroMenu(Screen):
    def __init__(self, **kw):
        super(MyCadastroMenu, self).__init__(**kw)
        
        self.layout = BoxLayout(orientation= 'vertical')
        
        self.lbl_titulo = Label(text="Bem vindo ao site de cadastro!", size_hint=(1, 0.5))
        
        self.btn_cadastro = Button(text="Cadastrar")
        self.btn_cadastro.bind(on_press=self.change_screen)
        
        self.btn_mostrar = Button(text="Mostrar Cadastros")
        self.btn_mostrar.bind(on_press=self.change_screen_mostrar)
                
        self.btn_sair = Button(text="Sair", size_hint=(1, 0.5))
        self.btn_sair.bind(on_press=self.change_screen_close)
        
        self.layout.add_widget(self.lbl_titulo)
        self.layout.add_widget(self.btn_cadastro)
        self.layout.add_widget(self.btn_mostrar)
        self.layout.add_widget(self.btn_sair)
        self.add_widget(self.layout)
        
    
    def change_screen(self, instance):
        self.manager.current = 'cadastro'
        
        
    def change_screen_mostrar(self, instance):
        self.manager.current = 'mostrar'
        
        
    def change_screen_close(self, instance):
        App.get_running_app().stop()
        