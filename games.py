import os
from dataclasses import dataclass


@dataclass
class Games:
    def __post_init__(self):
        self.games = self.get_games()

    @staticmethod
    def get_games():
        # read games.txt and return a list of games
        return [game.strip() for game in open("games.txt", "r").readlines()]
