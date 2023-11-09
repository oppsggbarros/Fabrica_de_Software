from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from editar import *
from excluir import * 
from cadastro import *


class Inicio(Screen):
    def __init__(self, **instance):
        super().__init__(**instance)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Bem-vindo ao Sistema de cadastro")
        button = Button(text="Cadastrar", on_press=self.sign_in)
        button_sair = Button(text='Sair', on_press=self.close_app)
        btn_edit = Button(text='Editar', on_press=self.edit)
        btn_delete = Button(text='Excluir', on_press=self.delete)
        
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(btn_edit)
        layout.add_widget(btn_delete)
        layout.add_widget(button_sair)
        self.add_widget(layout)

    
    def close_app(self, instance):
        App.get_running_app().stop()
    def sign_in(self, instance):
        self.manager.current = 'cadastro'
    def edit(self, instance):
        self.manager.current = 'editar'
    def delete(self, instance):
        self.manager.current = 'excluir'



