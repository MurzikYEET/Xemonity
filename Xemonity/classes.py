from time import sleep as delay
import sys
import os
if os.name == "nt":
    import msvcrt
else:
    import termios
    import tty

def open_alt_screen():
    sys.stdout.write("\x1b[?1049h")
    clear_screen()

def close_alt_screen():
    #clear_screen()
    sys.stdout.write("\x1b[?1049l")

def clear_screen():
    if is_windows():
        os.system('cls')
    else:
        os.system('clear')

def get_key_posix(): #for unix-like os (MacOS,Linux,*BSD and other)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == '\x1b': #Up or down
            ch += sys.stdin.read(2)
            if ch == '\x1b[A': return 'UP'
            if ch == '\x1b[B': return 'DOWN'
            return None
        elif ch == '\r': # Enter
            return 'ENTER'
        elif ch == '\x03': # Ctrl+C
            raise KeyboardInterrupt
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def get_key_nt(): #for NT-like os (Windows)
    ch = msvcrt.getch()
    if ch in (b'\x00', b'\xe0'): #Up or down
        ch = msvcrt.getch()
        if ch == b'H': return 'UP'
        if ch == b'P': return 'DOWN'
        return None

    if ch == b'\r': return 'ENTER' #Enter
    if ch == b'\x03': raise KeyboardInterrupt # Ctrl+C
        
    return ch.decode('utf-8', errors='ignore')

def is_windows():return os.name == "nt"

class XemonityAM:
    def __init__(self,elements:list,title:str):
        self.cursor = 0
        self.elements = elements
        self.elements.append(":Cancel")
        self.title = title
    def update_screen(self,intertime=0.05):
        clear_screen()
        print(self.title)
        if self.cursor >= 4:print("...")
        for i in range(0,len(self.elements)):
            if i+3 < self.cursor:
                continue
            if i == self.cursor: print(">>",end="")
            print(self.elements[i])
        delay(intertime)
    def relist(self,newlist:list):
        self.elements = newlist
        self.cursor = 0
    def show_sync(self):
        try:
            self.cursor = 0
            open_alt_screen()
            while True:
                self.update_screen()

                if is_windows():pressed = get_key_nt()
                else:pressed = get_key_posix()

                if pressed == "DOWN":
                    self.cursor += 1
                    if self.cursor >= len(self.elements):self.cursor = 0
                    self.update_screen()
                elif pressed == "UP":
                    self.cursor -= 1
                    if self.cursor <= -1:self.cursor = len(self.elements)-1
                    self.update_screen()
                elif pressed == "ENTER":
                    close_alt_screen()
                    return self.elements[self.cursor]
        except:
            close_alt_screen()
            return ":CANCELED"