from dataclasses import dataclass
import colorama

@dataclass
class Colors:
    def __init__(self):
        colorama.init()
        global YELLOW, RED, GREEN, RESET
        YELLOW = colorama.Fore.LIGHTYELLOW_EX
        RED = colorama.Fore.LIGHTRED_EX
        GREEN = colorama.Fore.LIGHTGREEN_EX
        RESET = colorama.Fore.RESET