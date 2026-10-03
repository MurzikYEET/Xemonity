# Xemonity
Xemonity - Python3 lib for simple menu with choose mained on pynput 
## How to use?
Code look as '''python
import Xemonity #import lib
am = Xemonity.XemonityAM(elements=["one","two","three"],"Its a title") #make class with elements and title
result = am.show_sync() #show menu (only sync) and return choosed string as str()
print(result) #print result to screen
'''
## Classes and methods
'Xemonity.XemonityAM(elements:list,title:str)'
Main class for menu
1. 'XemonityAM.cursor' : int var : return a current selected element index
2. 'XemonityAM.title' : str var : just a title, shows over elements
3. 'XemonityAM.elements' : list var : list of elements
4. 'XemonityAM.show_sync()' : str func : show menu and return choosed element
Other methods not for you
## Credits
[https://pypi.org/user/moses.palmer/](moses.palmer) : made pynput lib
## License
Licensed under MIT license