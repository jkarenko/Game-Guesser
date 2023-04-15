import textwrap
from random import choice

import openai

from games import Games

MODEL = "gpt-3.5-turbo"


def get_riddle():
    game = choice(Games.get_games())
    return openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system",
             "content": "Olet PC pelien arvuuttaja. Keksi arvoituksia, jotka sisältävät pelin nimen synonyyminä, pelin asetelman, juonen, ympäristön, hahmot ja tavoitteet. Omaksu pelin päähahmon rooli kun esität arvoituksen. Älä paljasta paikkojen tai henkilöiden nimiä."},
            {"role": "user", "content": "Overwatch"},
            {"role": "assistant",
             "content": "Tässä pelissä hyvä ja paha taistelevat, vaikkakin joskus myös samalla puolella. Kuolema ei ole pysyvä, vain hidaste, mutta et halua hidastetta kun sinulla on kiire päästä oman joukkueesi luokse ja kaapata hallintapiste tai palata saattotehtävään. Valitse yksi lukuisista sankareista ja taistele voittoon lentäen ja raketteja ampuen, juosten konetuliaseen laulaessa tai pysyttele taaempaana ja pidä ystäväsi elossa."},
            {"role": "user", "content": f"{game}"},
        ],
        temperature=0,
    ), game


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def wrap_text(text, max_line_length=80):
    return textwrap.wrap(text, width=max_line_length)


class Riddle:
    def __init__(self, game):
        self.game = game
        self.riddle = get_riddle()
        self.riddle = wrap_text(self.riddle)
        self.answer = self.get_answer()
        self.distance = self.levenshtein_distance(self.answer.lower(), self.game.lower())
        self.score = self.get_score()

    @classmethod
    def get_riddle(cls):
        riddle, game = get_riddle()
        riddle = riddle['choices'][0]['message']['content']
        riddle = wrap_text(riddle)
        return riddle, game

    @staticmethod
    def distance(s1, s2):
        return levenshtein_distance(s1, s2)
