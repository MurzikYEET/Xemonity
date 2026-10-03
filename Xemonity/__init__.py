from classes import *

if __name__ == "__main__":
    menu = XemonityAM(["One","Two","Three"],"Test menu")
    answer = menu.show_sync()
    print(answer)