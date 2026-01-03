from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlMouse():
    mouse = Controller()
    mouse.position = [10,20]

'''controlMouse()#both mouse and keyboard controller not 
used in pynput at a single time, only one controller is use at a time'''
def controlKeyboard():
    keyboard = Controller()
    keyboard.type('Hello World!')

controlKeyboard()
#controlling the mouse
#listening the mouse
#controlling the keyboard
#listening the keybard