from flask import Flask
from flask_ask import Ask, statement, convert_errors
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pyautogui as gui
import logging

app = Flask(__name__)
ask = Ask(app, '/')
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1000 per day"]
)

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('ForLoop', mapping={'numIterations': 'NumberIterations'}, default={'numIterations': '0'})
def for_loop(numIterations):
    gui.typewrite('for')
    gui.press('(')
    gui.typewrite('int i=0; i < ' + numIterations + ' ; i')
    gui.press(['+', '+', ')', '{'])
    gui.press(['enter', 'enter', '}', 'up', 'tab'])
    return statement('Wrote a loop!')
