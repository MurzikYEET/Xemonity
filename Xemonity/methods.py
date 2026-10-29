import os
import sys
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
        if ch == '\x1b': #Arrows
            ch += sys.stdin.read(2)
            if ch == '\x1b[A': return 'UP'
            if ch == '\x1b[B': return 'DOWN'
            if ch == '\x1b[C': return 'RIGHT'
            if ch == '\x1b[D': return 'LEFT'
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
    if ch in (b'\x00', b'\xe0'): #Arrows
        ch = msvcrt.getch()
        if ch == b'H': return 'UP'
        if ch == b'P': return 'DOWN'
        if ch == b'K': return 'LEFT'
        if ch == b'M': return 'RIGHT'
        return None

    if ch == b'\r': return 'ENTER' #Enter
    if ch == b'\x03': raise KeyboardInterrupt # Ctrl+C
        
    return ch.decode('utf-8', errors='ignore')

def get_key(): #universal
    if is_windows():return get_key_nt()
    else:return get_key_posix()

def min(minval,x):return x if x > minval else minval
def is_windows():return os.name == "nt"
def terminal_width():return os.get_terminal_size().columns
def terminal_height():return os.get_terminal_size().lines