# Xemonity documentation
## Classes
### `Xemonity.XemonityAM(elements:list,title:str)`
Main class for easy choose menu
- `XemonityAM.cursor` : int var : return a current selected element index
- `XemonityAM.title` : str var : just a title, shows before elements
- `XemonityAM.elements` : list var : list of elements (this is not recommended for modification)
- `XemonityAM.relist(newlist:list)` : None func : change list of elements
- `XemonityAM.show_sync()` : str func : show menu and return choosed element, if choosen ":Cancel" then method returns ":CANCELED"
### `Xemonity.XmntUIList(title="")'
Universal ui class
- `XmntUIList.title` : str var : just a title
- `XmntUIList.bind_action(action:str,method)` : None func : bind method (or None) to action
- `XmntUIList.connect_element(element)` : None func : connect `XUIL_Element` based class to `XmntUIList`
- `XmntUIList.connect_element_list(elements:list,clear_before=True)` : None func : clear all connects and connect new
- `XmntUIList.clear_elements_list()` : None func : clear all connects
- `XmntUIList.out_of()` : None func : exit from `show_sync()` method
- `XmntUIList.show_sync(intertime=0.25)` : dict func : show ui and return ui elements output. Example if created buttons with realname "hello" and "world" and presed "hello" button, then returns `{"hello":True,"world":False}`
### `Xemonity.XUIL_Element(realname,name="XmntUIList template")`
Main class for all ui elements
- `XUIL_Element.uilist` : XmntUIList var : link to parent `XmntUIList`
- `XUIL_Element.name` : str var : just a title
- `XUIL_Element.realname` : str var : ID for `XmntUIList.show_sync()`
- `XUIL_Element.stdout` : Any var : content, what must been showed in `XmntUIList.show_sync()` output
- `XUIL_Element.is_selected()` : bool func : returns `True` if cursor hovered on element
- `XUIL_Element.when_acted()` : None func : method called when arrow or enter pressed (its `UP DOWN LEFT RIGHT ENTER`)
- `XUIL_Element.render()` : None func : method called when `XmntUIList.show_sync()` try render element
## Elements
### `Button`
```python
class Button(
 realname: Any,
 title: str = "Button",
 on_click: Any | None = None
)
```
Default button. When pressed and `on_click` equals `None`, then `XmntUIList.show_sync()` breaks. When pressed and `on_click` equal method or lambda then `on_click` has been called. Return `True` if pressed, else `False`
### `Label`
```python
class Label(
 realname: Any,
 label: str = "I lable"
)
```
Default label
### `Checkbox`
```python
class Checkbox(
 realname: Any,
 name: str = "Checkbox",
 default: bool = False
)
```
Default checkbox. `default` its a default checkbox value
### `Slider`
```python
class Slider(
 realname: Any,
 name: str = "Slider",
 mini: int = 0,
 default: int = 50,
 maxi: int = 100,
 step: int = 1
)
```
Default slider.\ `mini` is miniman value.\ `default` is standart.\ `maxi` is maximal value.\ `step` is count of steps, made when pressed `LEFT` or `RIGHT`
## Methods
### `terminal_width()` 
Returns terminal columns count
### `terminal_height()`
Returns terminal rows count
### `is_windows()`
Returns True if current OS is Microsoft Windows
## Binds
### before update
Runned when `XmntUIList.show_sync()` start next iteration of cycle `while`
### after update
Runned before `XmntUIList.show_sync()` starts next iteration of cycle `while`