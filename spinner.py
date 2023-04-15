import sys
import threading
import time

from colors import Colors

colors = Colors()
from colors import RESET, YELLOW, GREEN, RED


class Spinner:
    def __init__(self):
        self.spinner_chars = "|/-\\"
        self.spinner_length = len(self.spinner_chars)
        self.running = False

    def spin(self):
        counter = 0
        while self.running:
            sys.stdout.write(
                "\r" + YELLOW + "Pieni hetki, keksitään arvoitusta..." + RESET + self.spinner_chars[
                    counter % self.spinner_length])
            sys.stdout.flush()
            counter += 1
            time.sleep(0.2)

    def start(self):
        self.running = True
        threading.Thread(target=self.spin).start()

    def stop(self):
        self.running = False
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.flush()
