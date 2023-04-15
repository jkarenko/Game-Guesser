import os

from games import Games
from colors import Colors
from spinner import Spinner
from riddle import Riddle

colors = Colors()
from colors import RESET, YELLOW, GREEN, RED

games = Games().get_games()
spinner = Spinner()

score = 0
questions = 5

# clear screen
os.system("cls" if os.name == "nt" else "clear")

for i in range(questions):
    spinner.start()
    riddle, game = Riddle.get_riddle()
    spinner.stop()
    print(f"{GREEN}Kysymys {i + 1}/{questions}: Arvaa pelin nimi{RESET}", end="\n")

    for line in riddle:
        print(line)

    answer = input(f"{YELLOW}Vastauksesi:{RESET} ")
    distance = Riddle.distance(answer.lower(), game.lower())
    if distance == 0:
        print(f"{GREEN}Täsmälleen oikein!{RESET}")
        print(f"{GREEN}Ansaitsit kaksi pistettä!{RESET}")
        score += 2
    elif distance < 5:
        print(f"{GREEN}Oikein!{RESET}")
        print(f"{GREEN}Arvauksesi oli tarpeeksi lähellä. Oikea vastaus oli: {RESET}{game}")
        print(f"{GREEN}Ansaitsit yhden pisteen!{RESET}")
        score += 1
    else:
        print(f"{RED}Väärin!{RESET}")
        print(f"{RED}Oikea vastaus oli: {RESET}{game}")
    print(f"{GREEN}Pisteet: {score}{RESET}", end="\n\n")

print(f"{GREEN}Peli päättyi!{RESET}")
print(f"{GREEN}Sait yhteensä {score} pistettä!{RESET}")
