import os

from games import Games
from colors import Colors
from spinner import Spinner
from riddle import Riddle
from random import sample

colors = Colors()
from colors import RESET, YELLOW, GREEN, RED

spinner = Spinner()

questions = 5


class GameRiddler:
    def __init__(self):
        self.score = 0
        self.answers = []
        self.parameters = {}
        self.questions = 5

    def main(self, selection):
        # os.system("cls" if os.name == "nt" else "clear")
        self.answers, self.parameters = Games().get_games(selection)
        self.answers = sample(self.answers, k=self.questions)

        for i, title in enumerate(self.answers):
            spinner.start()
            riddle = Riddle.get_riddle(title, self.parameters)
            spinner.stop()
            print(f"{GREEN}{i + 1}/{self.questions}: {self.parameters['question']}{RESET}", end="\n")

            for line in riddle:
                print(line)

            answer = input(f"{YELLOW}>>>{RESET} ")
            distance = Riddle.distance(answer.lower(), title.lower())
            if distance == 0:
                print(f"{GREEN}Correct!{RESET}")
                print(f"{GREEN}You earned two points.{RESET}")
                self.score += 2
            elif distance < len(title) // 5:
                print(f"{GREEN}Close enough! Correct answer was: {RESET}{title}")
                print(f"{GREEN}You earned one point.{RESET}")
                self.score += 1
            else:
                print(f"{RED}Wrong!{RESET}")
                print(f"{RED}Correct answer was: {RESET}{title}")
            print(f"{GREEN}Score: {self.score}{RESET}", end="\n\n")

        print(f"{GREEN}Game over!{RESET}")
        print(f"{GREEN}You earned a total of {self.score} points.{RESET}")

    def get_score(self):
        return self.score

    def get_answers(self):
        return self.answers

    def get_parameters(self):
        return self.parameters

    def get_questions(self):
        return self.questions

    def set_score(self, score):
        self.score = score

    def set_answers(self, answers):
        self.answers = answers

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_questions(self, questions):
        self.questions = questions
