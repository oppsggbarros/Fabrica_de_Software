from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
import mysql.connector

class MyCadastro(Screen):
    def __init__(self, **kw):
        super(MyCadastro, self).__init__(**kw)
        
        self.layout = BoxLayout(orientation="vertical")
        self.grid = GridLayout(cols=1, size_hint=(1, 1))
        
        self.inp_nome = TextInput(hint_text="Nome")
        self.inp_cpf = TextInput(hint_text="CPF", input_filter='int')
        self.inp_fone = TextInput(hint_text="Telefone")
        self.inp_email = TextInput(hint_text="E-mail")
        self.inp_senha = TextInput(hint_text="Senha", password=True)
        
        self.btn_confirm = Button(text="CONCLUA cadastro", font_size=25)
        self.btn_confirm.bind(on_press=self.ConfirmarCadastro)
        
        self.btn_voltar = Button(text="Voltar", size_hint=(1, 0.8))
        self.btn_voltar.bind(on_press=self.change_screen_voltar)
        
        self.grid.add_widget(self.inp_nome)
        self.grid.add_widget(self.inp_cpf)
        self.grid.add_widget(self.inp_fone)
        self.grid.add_widget(self.inp_email)
        self.grid.add_widget(self.inp_senha)
        self.grid.add_widget(self.btn_confirm)
        self.grid.add_widget(self.btn_voltar)
        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)
        
        # Configurar a conexão com o banco de dados MySQL
        self.conn = mysql.connector.connect(
            host='10.28.0.230',
            user='suporte',
            password='suporte',
            database='cadastros'
        )
        self.cursor = self.conn.cursor()

    def ConfirmarCadastro(self, instance):
        self.nome = self.inp_nome.text
        self.cpf = self.inp_cpf.text
        self.fone = self.inp_fone.text
        self.email = self.inp_email.text
        self.senha = self.inp_senha.text
        
        # Inserir os dados no banco de dados
        query = "INSERT INTO tabela_cadastro (nome, cpf, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)"
        values = (self.nome, self.cpf, self.fone, self.email, self.senha)
        self.cursor.execute(query, values)
        self.conn.commit()
        
        print("Cadastro realizado com sucesso!")

    def change_screen_voltar(self, instance):
        self.inp_nome.text = ""
        self.inp_cpf.text = ""
        self.inp_fone.text = ""
        self.inp_email.text = ""
        self.inp_senha.text = ""
        self.manager.current = 'menu'
        
    def ExcluirCadastro(self, instance):
        cpf_excluir = self.inp_cpf.text

        
        query_select = "SELECT * FROM tabela_cadastro WHERE cpf = %s"
        self.cursor.execute(query_select, (cpf_excluir,))
        user_data = self.cursor.fetchone()

        if user_data:
            
            query_delete = "DELETE FROM tabela_cadastro WHERE cpf = %s"
            self.cursor.execute(query_delete, (cpf_excluir,))
            self.conn.commit()

            print("Cadastro excluído com sucesso!")
        else:
            
            self.mostrar_mensagem_erro("CPF não encontrado.")

    def mostrar_mensagem_erro(self, mensagem):
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text=mensagem))
        popup = Popup(title="Erro", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyCadastro(name='cadastro'))
        return sm

if __name__ == '__main__':
    MyApp().run()
