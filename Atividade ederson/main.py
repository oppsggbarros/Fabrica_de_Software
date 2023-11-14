from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from cadastro import MyCadastro
from menu import MyCadastroMenu
from voltar import MyCadastroMostrar

class MyCadastroMain(App):
    def build(self):
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(MyCadastroMenu(name='menu'))
        screen_manager.add_widget(MyCadastroMostrar(name='mostrar'))
        screen_manager.add_widget(MyCadastro(name='cadastro'))
        return screen_manager
    
    
if __name__ == '__main__':
    MyCadastroMain().run()