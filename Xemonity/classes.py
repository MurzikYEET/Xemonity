from time import sleep as delay
try:from .methods import *
except:from methods import *

try:
    import colorama
    support_colorama = True
except:
    support_colorama = False

class XemonityAM:
    def __init__(self,elements:list,title:str,append_cancel=True):
        """WARNING : this class deprecated, please use XmntUIList with Button class"""
        self.cursor = 0
        self.elements = elements
        if append_cancel:self.elements.append(":Cancel")
        self.title = title
    def update_screen(self,intertime=0.05):
        clear_screen()
        print(self.title)
        if self.cursor >= 4:print("...")
        for i in range(0,len(self.elements)):
            if i+3 < self.cursor:continue
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
                pressed = get_key()

                match pressed:
                    case "DOWN":
                        self.cursor += 1
                        if self.cursor >= len(self.elements):self.cursor = 0
                        self.update_screen()
                    case "UP":
                        self.cursor -= 1
                        if self.cursor <= -1:self.cursor = len(self.elements)-1
                        self.update_screen()
                    case "ENTER":
                        close_alt_screen()
                        return self.elements[self.cursor]
        except:
            close_alt_screen()
            return ":CANCELED"

class XmntUIList:
    def __init__(self,title=""):
        self.title = title
        self.elements = []
        self.cursor = 0

        self._bupdate = None
        self._aupdate = None

        self._breakme = False
    def bind_action(self,action:str,method):
        """Adds method for action (name of actions watch in DOCS.md)"""
        match action.lower():
            case "before update":self._bupdate = method
            case "after update":self._aupdate = method
            case _:raise Exception("Undefined action")
    def connect_element(self,element):
        """Add new element"""
        element.uilist = self
        self.elements.append(element)
    def clear_elements_list(self):
        """Remove all elements"""
        for i in self.elements:i.uilist = None
        self.elements.clear()
    def connect_element_list(self,elements:list,clear_before=True):
        """Clears list of elements and add new"""
        if clear_before:self.clear_elements_list()
        for i in elements:
            self.connect_element(i)
    def out_of(self):
        """Stop XmntUIList.show_sync()"""
        self._breakme = True
    def update_screen(self):
        clear_screen()
        if support_colorama:
            print(colorama.Back.WHITE+
                  (self.title[:terminal_width()])+
                  (" " * (terminal_width() - len(self.title))))
            print(colorama.Style.RESET_ALL,end="")
        else:
            print(self.title[:terminal_width()]+
                  ("_" * min(0,terminal_width() - len(self.title))))
        
        visible_height = terminal_height() - 2
        if visible_height < 1: visible_height = 1
        
        offset = 0
        if self.cursor >= visible_height:
            offset = self.cursor - visible_height + 1

        for i in range(offset, offset + visible_height):
            if i >= len(self.elements):
                break
            if i == self.cursor:print("::",end="")
            else: print("  ",end="")
            self.elements[i].render()
    def show_sync(self,intertime=0.05):
        """Show interface"""
        while True:
            if self._bupdate != None:self._bupdate()
            if self._breakme:
                self._breakme = False
                break
            self.update_screen()
            try:pr = get_key()
            except KeyboardInterrupt:
                self._breakme = True
                continue

            match pr:
                case "DOWN":
                    if self.cursor >= len(self.elements)-1:self.cursor = 0
                    else:self.cursor += 1
                    self.elements[self.cursor].when_acted("DOWN")
                case "UP":
                    if self.cursor <= 0:self.cursor = len(self.elements)-1
                    else:self.cursor -= 1
                    self.elements[self.cursor].when_acted("UP")
                case "ENTER":
                    self.elements[self.cursor].when_acted("ENTER")
                case "LEFT":
                    self.elements[self.cursor].when_acted("LEFT")
                case "RIGHT":
                    self.elements[self.cursor].when_acted("RIGHT")
            if self._aupdate != None:self._aupdate()
            delay(intertime)
        to_out = {}
        for i in self.elements:
            to_out[i.realname] = i.stdout
        clear_screen()
        close_alt_screen()
        return to_out

class XUIL_Element:
    def __init__(self,realname,name="XmntUIList template"):
        """Main class for all UI elements"""
        self.uilist:XmntUIList = None
        self.name = name
        self.realname = realname
        self.stdout = ""
    def is_selected(self):
        """Return true if cursor in element"""
        return self.uilist.elements.count(self) >= 1
    def when_acted(self,action:str):
        """Called when user press arrows, enter and other buttons registred in get_key() method"""
    def render(self):
        """Called when XmntUIList.show_sync() try draw look"""
        print(self.name)

class Button(XUIL_Element):
    def __init__(self,realname,title="Button",on_click=None):
        super().__init__(realname,title)
        self.on_click = on_click
        self.stdout = False
    def when_acted(self, action):
        if action == "ENTER":
            self.stdout = True
            if self.on_click:self.on_click()
            else:self.uilist.out_of()
    def render(self):
        print("|"+self.name+"|")

class Label(XUIL_Element):
    def __init__(self, realname, label="I lable"):
        super().__init__(realname, label)
        self.label = label
    def render(self):
        print(self.label[:terminal_width() - (2 if self.is_selected else 0)])

class Checkbox(XUIL_Element):
    def __init__(self, realname, name="Checkbox",default=False):
        super().__init__(realname, name)
        self.stdout = default
    def when_acted(self, action):
        if action == "LEFT" or action == "RIGHT" or action == "ENTER":
            self.stdout = not self.stdout
    def render(self):
        print(self.name + " : " + ("▉▉" if self.stdout else "░░"))

class Slider(XUIL_Element):
    def __init__(self, realname, name="Slider", mini=0, default=50, maxi=100, step=1):
        super().__init__(realname, name)
        self.min = mini
        self.max = maxi
        self.stdout = default
        self.step = step
    def when_acted(self, action):
        if action == "LEFT":self.stdout = self.stdout if self.stdout < (self.min + self.step) else self.stdout - self.step
        if action == "RIGHT":self.stdout = self.stdout if self.stdout > (self.max - self.step) else self.stdout + self.step
    def render(self):
        normalized = (self.stdout - self.min) / (self.max - self.min)
        bar_width = terminal_width() - len(self.name) - len(str(self.stdout)) - 7
        to_fill = int(normalized * bar_width)
        to_skip = bar_width - to_fill
        print(self.name + f"({self.stdout})" + ":::" + ("▉" * to_fill) + ("░" * to_skip))