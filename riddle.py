import textwrap
from random import choice

import openai
import re

from games import Games

MODEL = "gpt-3.5-turbo"


def get_riddle(title: str, parameters: dict):
    return openai.ChatCompletion.create(
        model=parameters["model"] if "model" in parameters else MODEL,
        messages=[
            {"role": "system", "content": parameters["system"]},
            {"role": "user", "content": f"{parameters['prompt']} {title}"},
        ],
        temperature=parameters.get("temperature", 0.5),
    )


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

    @classmethod
    def get_riddle(cls, title, parameters):
        riddle = get_riddle(title, parameters)
        riddle = riddle['choices'][0]['message']['content']
        return wrap_text(riddle)

    @staticmethod
    def distance(s1, s2):
        pattern = r"\s\(\d{4}\)"
        s2 = re.sub(pattern, "", s2)
        return levenshtein_distance(s1, s2)
