from client import ClientInfo
from connection import Connection, make_league_headers, endpoint
from util import formated
from api import *
import PySimpleGUI as gui

title = "Who's next?"

layout = [[gui.Text("me trollearan la ranked?")], 
          [gui.Button("D:")]]

margins = (150, 70)

if __name__ == "__main__":
    window = gui.Window(title=title, layout=layout, margins=margins)
    while True:
        event, values = window.read()
        if event == "D:":
            req = API()
            teammates = req.get_ranked_players()
            req.query_opgg()
        elif event == gui.WIN_CLOSED:
            break
    window.close()
        
