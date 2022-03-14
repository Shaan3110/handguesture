from flask import Flask
import keyboard
import time

app = Flask(__name__)


def copypaste():
    keyboard.press_and_release('ctrl + a')
    keyboard.press_and_release('ctrl + c')
    keyboard.press_and_release('ctrl + v')
    time.sleep(3)
    return 0