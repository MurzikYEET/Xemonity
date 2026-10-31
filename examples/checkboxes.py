from Xemonity import *

if __name__ == "__main__":
    ls = XmntUIList(title="Policy")
    ls.connect_element(Checkbox("policy","I agree conditions"))
    ls.connect_element(Checkbox("telemetry","I agree telemetry"))
    ls.connect_element(Button("next","Next"))
    print(ls.show_sync())