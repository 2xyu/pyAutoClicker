import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key

TOGGLE_KEY = Key.ctrl_r

class Clicker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.clicking = False
        self.mouse = Controller()

    def run(self):
        while True:
            if self.clicking:
                self.mouse.click(Button.left, 1)
            time.sleep(0.025)

    def toggle_clicking(self):
        self.clicking = not self.clicking

clicker = Clicker()
clicker.start()

def toggle_event(key):
    if key == TOGGLE_KEY:
        clicker.toggle_clicking()

with Listener(on_press=toggle_event) as listener:
    listener.join()
