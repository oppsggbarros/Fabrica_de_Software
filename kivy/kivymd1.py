import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1, 1))

        self.text_input = TextInput(text = 'Digite seu Nome')
        grid.add_widget(self.text_input)

        button1 = Button(text = 'Apagar')
        grid.add_widget(button1)
        button1.bind(on_press = self.apagar_text)

        button2 = Button(text = 'Verificar')
        button2.bind(on_press = self.text)
        grid.add_widget(button2)

        layout.add_widget(grid)

        return layout
    def apagar_text(self, instance):
        self.text_input.text = ''
    
    def text(self, instance):
        if self.text_input.text == 'Gabriel':
            self.text_input.text = 'Ele é bunito'
        elif self.text_input.text == '':
            self.text_input.text = ''
        else:
            self.text_input.text = 'Ele é feio'

if __name__ == '__main__':    
    firstBotao().run()