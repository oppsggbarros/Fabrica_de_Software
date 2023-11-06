import kivy
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class WannaPlayScreen(Screen):
    def on_yes_pressed(self):
        self.manager.current = 'guess_choice'

    def on_no_pressed(self):
        App.get_running_app().stop()

class GuessesScreen(Screen):
    def on_yes_pressed(self):
        self.manager.get_screen('time_to_guess').set_text()
        self.manager.current = 'time_to_guess'
        App.get_running_app().guesses_left = 3
        self.manager.get_screen('time_to_guess').ids.guesses_left.text = App.get_running_app().guess_text

class TimeToGuessScreen(Screen):
    def set_text(self):
        self.ids.label.text = "Guess a number between 1 and 10"

    def on_number_pressed(self, number):
        App.get_running_app().user_guess = number
        App.get_running_app().guesses_left -= 1
        self.ids.guesses_left.text = 'Guesses Left: ' + str(App.get_running_app().guesses_left)
        if App.get_running_app().user_guess == App.get_running_app().random_num:
            self.manager.current = 'winner'
        elif (App.get_running_app().user_guess != App.get_running_app().random_num) and (App.get_running_app().guesses_left == 0):
            self.manager.current = 'loser'

class WinnerScreen(Screen):
    def on_yes_pressed(self):
        App.get_running_app().guesses_left = 3
        self.manager.current = 'guess_choice'
        App.get_running_app().computer_num = random.randint(1, 10)
        App.get_running_app().random_num = str(App.get_running_app().computer_num)

    def on_no_pressed(self):
        App.get_running_app().stop()

class LoserScreen(Screen):
    def on_yes_pressed(self):
        self.manager.current = 'guess_choice'
        App.get_running_app().computer_num = random.randint(1, 10)
        App.get_running_app().random_num = str(App.get_running_app().computer_num)

    def on_no_pressed(self):
        App.get_running_app().stop()

class GuessingGameApp(App):
    computer_num = random.randint(1, 10)
    random_num = str(computer_num)
    guesses_left = 3
    user_guess = None
    guess_text = ''

    def build(self):
        sm = ScreenManager()

        start_screen = WannaPlayScreen(name='start')
        start_screen.add_widget(GridLayout(cols=1, children=[
            Label(text='Want to Play the Guessing Game?'),
            GridLayout(cols=2, children=[
                Button(text='Yes', on_release=lambda instance: start_screen.on_yes_pressed()),
                Button(text='No', on_release=lambda instance: start_screen.on_no_pressed()),
            ]),
        ]))

        guess_choice_screen = GuessesScreen(name='guess_choice')
        guess_choice_screen.add_widget(GridLayout(cols=1, children=[
            Label(text='You Will Have 3 guesses. Are You Ready?'),
            Button(text='YES', on_release=lambda instance: guess_choice_screen.on_yes_pressed()),
        ]))

        time_to_guess_screen = TimeToGuessScreen(name='time_to_guess')
        time_to_guess_screen.add_widget(GridLayout(cols=1, children=[
            Label(id='label', text=''),
            Label(id='guesses_left', text=''),
            GridLayout(cols=5, children=[
                Button(text=str(i), on_release=lambda instance, i=i: time_to_guess_screen.on_number_pressed(str(i)))
                for i in range(1, 11)
            ]),
        ]))

        winner_screen = WinnerScreen(name='winner')
        winner_screen.add_widget(GridLayout(cols=1, children=[
            Label(text='You have Won!'),
            Label(text='Would You Like To Play Again?'),
            GridLayout(cols=2, children=[
                Button(text='Yes', on_release=lambda instance: winner_screen.on_yes_pressed()),
                Button(text='No', on_release=lambda instance: winner_screen.on_no_pressed()),
            ]),
        ]))

        loser_screen = LoserScreen(name='loser')
        loser_screen.add_widget(GridLayout(cols=1, children=[
            Label(text='You have Lost!'),
            Label(text='Would You Like To Play Again?'),
            GridLayout(cols=2, children=[
                Button(text='Yes', on_release=lambda instance: loser_screen.on_yes_pressed()),
                Button(text='No', on_release=lambda instance: loser_screen.on_no_pressed()),
            ]),
        ]))

        sm.add_widget(start_screen)
        sm.add_widget(guess_choice_screen)
        sm.add_widget(time_to_guess_screen)
        sm.add_widget(winner_screen)
        sm.add_widget(loser_screen)

        return sm

if __name__ == '__main__':
    GuessingGameApp().run()
