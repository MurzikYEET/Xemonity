try: 
    from .classes import *
except ImportError:
    from classes import *

if __name__ == "__main__":
    menu = XemonityAM(["One","Two","Three","Four","Five","Six","Seven"],"Test menu")
    answer = menu.show_sync()
    print(answer)
    menu.elements = ["Yes","No"]
    answer = menu.show_sync()
    print(answer)