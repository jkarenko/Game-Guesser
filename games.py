from dataclasses import dataclass
import tomllib
import imdb_reader

@dataclass
class Games:

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
                print(f"Reading file {parameters['files']}")
                answers = imdb_reader.imdb_reader(parameters["files"])

        else:
            answers = [line.strip() for file in parameters["files"] for line in open(file, 'r')]

        return answers, parameters
