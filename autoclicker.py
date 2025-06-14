import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Config variables
d = 0.001             # Delay between clicks
btn = Button.left     # Mouse button to click

# Hotkeys
start_key = KeyCode(char='a')  # Start/stop key
exit_key = KeyCode(char='b')   # Exit key

class AutoClicker(threading.Thread):
    def __init__(self, d, btn):
        super().__init__()
        self.d = d
        self.btn = btn
        self.clicking = False
        self.active = True

    def start_click(self):
        self.clicking = True

    def stop_click(self):
        self.clicking = False

    def exit(self):
        self.stop_click()
        self.active = False

    def run(self):
        while self.active:
            while self.clicking:
                mouse.click(self.btn)
                time.sleep(self.d)

# Create mouse controller
mouse = Controller()

# Create and start the auto-clicker thread
clicker = AutoClicker(d, btn)
clicker.start()

# Keyboard listener function
def on_press(k):
    if k == start_key:
        if clicker.clicking:
            clicker.stop_click()
            print("[INFO] Clicker Stopped.")
        else:
            clicker.start_click()
            print("[INFO] Clicker Started.")
    elif k == exit_key:
        clicker.exit()
        print("[INFO] Exiting.")
        return False  # Stop listener

# Start listening for keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()
