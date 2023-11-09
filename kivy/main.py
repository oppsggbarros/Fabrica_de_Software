from screenmanagers import *

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicio(name='começo'))
        sm.add_widget(In_game(name='jogo'))
        return sm

if __name__ == '__main__':
    MyApp().run()