from Xemonity import *

ls = XmntUIList(title="Soundmixer")
ls.connect_element(Slider("speaker","Speaker1",mini=0,default=90,maxi=100,step=5))
ls.connect_element(Slider("micro","Microphone1"))
ls.connect_element(Button("commit","Commit",lambda:print("Commited!")))
print(ls.show_sync())