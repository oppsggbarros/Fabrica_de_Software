from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from in_games import In_game


class Inicio(Screen):
    def __init__(self, **instance):
        super().__init__(**instance)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Bem-vindo ao Jogo")
        button = Button(text="Jogar")
        button_sair = Button(text='Sair')
        button_sair.bind(on_press=self.close_app)
        button.bind(on_press=self.switch_to_info)
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(button_sair)
        self.add_widget(layout)

    def switch_to_info(self, instance):
        self.manager.current = 'jogo'

    def close_app(self, instance):
        App.get_running_app().stop()




