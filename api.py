from client import ClientInfo
from connection import Connection, make_league_headers, make_riot_headers, endpoint
from util import formated
import json
import logging
import webbrowser

logging.basicConfig(filename="whosnext.log", encoding="utf-8", level=logging.DEBUG)
    
class API:
    def __init__(self):
        self.league_info = ClientInfo()
        self.riot_info = ClientInfo(riot_client=True)

    def get_skins(self):
        url=endpoint("skins", self.league_info.port)
        headers=make_league_headers(self.league_info)
        try:
            return Connection.request(url, headers).decode("utf-8")
        except Exception as e:
            logging.error(f"while retrieving skins information:\n{e.msg}")
            print("No fue posible obtener lista de skins")
            return ""

    def get_teammates(self):    
        url = endpoint("champion_select", self.league_info.port)
        headers = make_league_headers(self.league_info)
        try:
            data = Connection.request(url, headers).decode("utf-8")
            load = json.loads(data)
            return load["myTeam"]
        except Exception as e:
            logging.error(f"while retrieving teammates information:\n{e.msg}")
            print("No fue posible obtener informacion de compañeros")
            return ""
    
    def get_player_name_by_id(self, player_id):
        url= endpoint("player", self.league_info.port, player_id)
        headers = make_league_headers(self.league_info)
        try:
            data = Connection.request(url, headers).decode("utf-8")
            load = json.loads(data)
            return load
        except Exception as e:
            logging.error(f"while retrieving player name by id:\n{e.msg}")
            print("no fue posible conseguir informacion de jugador")
            return ""
        
    def get_ranked_players(self):
        headers = make_riot_headers(self.riot_info)
        url = endpoint("ranked_select", self.riot_info.port)
        try:
            data = Connection.request(url, headers).decode("utf-8")
            load = json.loads(data)
            players_info = load["participants"]
            return ",".join([player_info["name"] for player_info in players_info])
        except:
            logging.error("while retrieving ranked teammates")
            print("no fue posible conseguir informacion de compañeros[clasificatoria]")
            return ""

    def query_opgg(self):
        players_string = self.get_ranked_players()
        url = "https://las.op.gg/multi/query=" + players_string
        webbrowser.open(url)
