from Xemonity import *

if __name__ == "__main__":
    ls = XmntUIList(title="Setup")
    ls.connect_element(Inputbox("inputer","Name"))
    ls.connect_element(Dropdown("aaa","Type",{"cool":"Cool","coffee":"Coffee","whoami":"Who am i?"}))
    print(ls.show_sync())