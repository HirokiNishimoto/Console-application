import pyautogui as pgui

#:wdef replace(word):
    

def _typewrite(word):
    word = wprd.replace("","")



def spotlight(word):
    word = str(word)
    pgui.keyDown('command')
    pgui.keyDown('space')
    pgui.keyUp('space')
    pgui.keyUp('command')
    pgui.typewrite(word)
    pgui.keyDown('enter')
    pgui.keyUp('enter')

def cmd_(button):
    """
    arg: strings
    return: none
    """
    pgui.keyDown('command')
    pgui.keyDown(button)
    pgui.keyUp(button)
    pgui.keyUp('command')















"""
#chromeを開く
spotlight("chrome")

#chrome->github
pgui.keyDown('command')
pgui.keyDown('t')
pgui.keyUp('t')
pgui.keyUp('command')
pgui.typewrite("https'//github.com/HirokiNishimoto") 
#pgui.typewrite("#:' , +:* , <:>")
pgui.keyDown('enter')
pgui.keyUp('enter')
"""
