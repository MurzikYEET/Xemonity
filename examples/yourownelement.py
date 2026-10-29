from Xemonity import *

class MyElement(XUIL_Element):
    def __init__(self, realname, label="hi"):
        super().__init__(realname, label)
        self.label = label
    def render(self):
        print(self.label[:terminal_width() - (2 if self.is_selected else 0)])

if __name__ == "__main__":
    list = XmntUIList()
    list.connect_element(MyElement("hello"))
    list.show_sync()