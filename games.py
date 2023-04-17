from dataclasses import dataclass
import tomllib
from imdb_reader import IMDBReader


@dataclass
class Games:
    reader = None

    @staticmethod
    def get_games(category_choice: str = None):
        print(f"category_choice: {category_choice}")
        with open("config.toml", "rb") as f:
            config = tomllib.load(f)
        topic = category_choice
        print(f"topic: {topic}")
        parameters = config[topic]
        if "reader" in parameters:
            reader = parameters["reader"]
            print(f"reader: {reader}")
            if reader == "imdb":
                if Games.reader is None:
                    print(f"Reading data from {parameters['files']}")
                    Games.reader = IMDBReader(parameters["files"], parameters["type"])
                answers = Games.reader.get_titles()
        else:
            answers = [line.strip() for file in parameters["files"] for line in open(file, 'r')]

        return answers, parameters
