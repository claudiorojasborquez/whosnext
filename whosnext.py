from client import ClientInfo, ClientInfoError
from connection import Connection, make_league_headers, endpoint
from util import formated
from api import *
import PySimpleGUI as gui
import win32gui, win32con

gui.theme("dark purple")
gui.set_options(element_padding=(5,5))
title = "Who's next?"

def name(name):
    NAME_SIZE = 27
    spaces = NAME_SIZE-len(name)-2
    return gui.Text(name + " "*spaces, size=(NAME_SIZE,1), justification="l")

def button(name):
    return gui.Button(name, size=button_size, pad=(5,5), border_width=1)

button_size = 30
layout = [[gui.Image("assets/death64.png"), gui.Text("Who's next?", font="_ 20 bold", justification="r")], 
          [name("op.gg"), gui.Radio("", group_id=1, key="opgg")],
          [name("u.gg"), gui.Radio("", group_id=1, key="ugg")],
          [name("porofessor"), gui.Radio("", group_id=1, key="porofessor")],
          [name("poro"), gui.Radio("", group_id=1, key="poro")],
          [button("¿Quién me trollea hoy?")],
          [button("Reiniciar")]]

icon="assets/ico/16.ico"

margins = (15, 15)

search_options=["opgg", "ugg", "porofessor", "poro"]

if __name__ == "__main__":
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)
    req = API()
    window = gui.Window(title=title, layout=layout, margins=margins, icon=icon)
    while True:
        event, values = window.read()
        if event == "¿Quién me trollea hoy?":
            site=None
            for op in search_options:
                if values[op]:
                    site=op
            try:
                req.search_web(site=site)
            except ClientInfoError as e:
                if e.code == -1:
                    gui.popup("No hay cliente del LOL activo")
                    continue
                else:
                    raise e
                
        elif event == "Reiniciar":
            req = API()

        elif event == gui.WIN_CLOSED:
            break
    window.close()
        
