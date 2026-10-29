# Xemonity documentation
## Classes
### `Xemonity.XemonityAM(elements:list,title:str)`
Main class for easy choose menu
1. `XemonityAM.cursor` : int var : return a current selected element index
2. `XemonityAM.title` : str var : just a title, shows before elements
3. `XemonityAM.elements` : list var : list of elements (this is not recommended for modification)
4. `XemonityAM.relist(newlist:list)` : None func : change list of elements
5. `XemonityAM.show_sync()` : str func : show menu and return choosed element, if choosen ":Cancel" then method returns ":CANCELED"
### `Xemonity.XmntUIList(title="")'
Universal ui class
1. `XmntUIList.title` : str var : just a title
2. `XmntUIList.connect_element(element)` : None func : connect `XUIL_Element` based class to `XmntUIList`
3. `XmntUIList.clear_elements_list()` : None func : clear all connects
4. `XmntUIList.out_of()` : None func : exit from `show_sync()` method
5. `XmntUIList.show_sync(intertime=0.25)` : dict func : show ui and return ui elements output. Example if created buttons with realname "hello" and "world" and presed "hello" button, then returns `{"hello":True,"world":False}`
### `Xemonity.XUIL_Element(realname,name="XmntUIList template")`
Main class for all ui elements
1. `XUIL_Element.uilist` : XmntUIList var : link to parent `XmntUIList`
2. `XUIL_Element.name` : str var : just a title
3. `XUIL_Element.realname` : str var : ID for `XmntUIList.show_sync()`
4. `XUIL_Element.stdout` : Any var : content, what must been showed in `XmntUIList.show_sync()` output
5. `XUIL_Element.is_selected()` : bool func : returns `True` if cursor hovered on element
6. `XUIL_Element.when_acted()` : None func : method called when arrow or enter pressed (its `UP DOWN LEFT RIGHT ENTER`)
7. `XUIL_Element.render()` : None func : method called when `XmntUIList.show_sync()` try render element
## Elements
### `Button(realname,title="Button")`
Default button, when pressed XmntUIList.show_sync() breaks. Return True if pressed, else False
### `Label(realname,label="template")
Default label
## Methods
### `terminal_width()` 
Returns terminal columns count
### `terminal_height()`
Returns terminal rows count
### `is_windows()`
Returns True if current OS is windows