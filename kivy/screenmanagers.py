from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
import secrets as sc

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

class In_game(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="", valign='top')
        self.text_input = TextInput(hint_text='Digite um número', input_filter='int')
        button = Button(text="Voltar")
        button.bind(on_press=self.switch_to_welcome)
        btn_verifica = Button(text='Verificar')
        btn_verifica.bind(on_press=self.verifica)
        btn_reiniciar = Button(text='Reiniciar')
        btn_reiniciar.bind(on_press=self.reiniciar)
        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(btn_verifica)
        layout.add_widget(btn_reiniciar)
        layout.add_widget(button)
        self.add_widget(layout)
        self.reiniciar()

    def switch_to_welcome(self, *args):
        self.manager.current = 'começo'
        
    def reiniciar(self, *args):
        self.number = sc.randbelow(100)
        self.label.text = ""  
        self.text_input.text = ""  
    def verifica(self, instance):
        guess = int(self.text_input.text)  
        try:
            guess = int(self.text_input.text)
            if guess == self.number:
                self.label.text = 'Parabéns! Você acertou!'
            elif guess < self.number:
                self.label.text = 'O número é maior'
            elif guess > self.number:
                self.label.text = 'O número é menor'
        except ValueError:
            self.label.text = 'Por favor, insira um número válido.'
        
        
        

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicio(name='começo'))
        sm.add_widget(In_game(name='jogo'))
        return sm

if __name__ == '__main__':
    MyApp().run()
