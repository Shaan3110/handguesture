from flask import Flask
import keyboard
import time

app = Flask(__name__)


@app.route('/copy-paste', methods=['POST'])
def copypaste():
    keyboard.press_and_release('ctrl + a')
    keyboard.press_and_release('ctrl + c')
    keyboard.press_and_release('ctrl + v')
    time.sleep(3)
    return 0


if __name__=="__main__":
    app.run(debug=True,port=3000)