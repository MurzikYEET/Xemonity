from Xemonity import *

if __name__ == "__main__":
    mixer = XmntUIList("АЙАЙАЙАЙАЙАЙАЙАЙ УБИЛИ РУБЛЬ УБИЛИ РУБЛЬ ГАДЫ")
    mixer.connect_element(Button("btn","fffff"))
    mixer.connect_element(Button("btn_1","лорд жиробас"))
    mixer.connect_element(Button("btn_2","Йозеф 200"))
    mixer.connect_element(Label("lbl","ГНУ СЛОП МЮСЛ И ХУРД ЛУЧШЕ ВИРУС СИСТЕМД ОТ РЕДХАТ ОПЕН СУРС ГДЕ ОПЕНСУРС ДА ЗАВАЛИСЬ БЖЕ ЛАРП ЛАРП ЛАРП ЛАПР ЛАРП ЛАРП САХУР ГНУ СЛОП МЮСЛ И ХУРД ЛУЧШЕ ВИРУС СИСТЕМД ОТ РЕДХАТ ОПЕН СУРС ГДЕ ОПЕНСУРС ДА ЗАВАЛИСЬ БЖЕ ЛАРП ЛАРП ЛАРП ЛАПР ЛАРП ЛАРП САХУР"))
    for i in range(20):
        mixer.connect_element(Button("btn_c"+str(i),"Кнопка"+str(i)))
    mixer.connect_element(Button("ggggg","Шуй 67"))
    a = mixer.show_sync()
    print(a)