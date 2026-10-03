from pynput import keyboard
from time import sleep as delay
import sys
import os

#def on_next():return pynput.keyboard.Listener.
#def on_prev():return keyboard.is_pressed("up")
#def on_enter():return keyboard.is_pressed("enter")

def open_alt_screen():
    sys.stdout.write("\x1b[?1049h")
    clear_screen()

def close_alt_screen():
    #clear_screen()
    sys.stdout.write("\x1b[?1049l")

def clear_screen():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Linux и macOS
    else:
        os.system('clear')

class XemonityAM:
    def __init__(self,elements:list,title:str):
        self.cursor = 0
        self.elements = elements
        self.title = title
    def update_screen(self,intertime=0.25):
        clear_screen()
        print(self.title)
        for i in range(0,len(self.elements)):
            if i == self.cursor: print(">>",end="")
            print(self.elements[i])
        delay(intertime)
    def on_press(self,key:keyboard.Key):
        try:
            if key == keyboard.Key.down:
                self.cursor += 1
                if self.cursor >= len(self.elements):
                    self.cursor = 0
                self.update_screen()
            elif key == keyboard.Key.up:
                self.cursor -= 1
                if self.cursor <= -1:
                    self.cursor = len(self.elements)-1
                self.update_screen()
            elif key == keyboard.Key.enter:
                close_alt_screen()
                self.returned = self.elements[self.cursor]
                return False
        except AttributeError:
            pass#print(f'Нажата спецклавиша: {key}')
    def on_release(self,key):
        if key == keyboard.Key.esc:
            return False
    def show_sync(self):
        open_alt_screen()
        self.update_screen()
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        return self.elements[self.cursor]