from screenmanagers import *
import secrets as sc


class In_game(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Digite um número entre 1 a 100", valign='top')
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
        self.label.text = "Digite um número entre 1 a 100"  
        self.text_input.text = ""  
    def verifica(self, instance):
        guess = int(self.text_input.text)  
        try:
            guess = int(self.text_input.text)
            if guess == self.number:
                self.label.text = 'Você ganhou!'
            elif guess < self.number:
                self.label.text = 'O número é maior'
            elif guess > self.number:
                self.label.text = 'O número é menor'
        except ValueError:
            self.label.text = 'Por favor, insira um número válido.'