import urllib.request
import ssl
import webbrowser

def make_league_headers(info):
    return {
        "Host" : "127.0.0.1:" + info.port,
		"Connection": "keep-alive",
		"Authorization": "Basic " + info.token,
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Origin": "https://127.0.0.1:" + info.port,
		"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) LeagueOfLegendsClient/" + info.version + " (CEF 91) Safari/537.36",
		"X-Riot-Source": "rcp-fe-lol-social",
		"sec-ch-ua": "\"Chromium\";v=\"91\"",
		"sec-ch-ua-mobile": "?0",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://127.0.0.1:" + info.port + "/index.html",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "en-US,en;q=0.9",
        "Cookies" : ""
        }

def make_riot_headers(info):
    return {
        "Host":"127.0.0.1:"+ info.port,
		"Connection": "keep-alive",
		"Authorization": "Basic " + info.token ,
		"Accept":"application/json",
		"Access-Control-Allow-Credentials":"true",
		"Access-Control-Allow-Origin":"127.0.0.1",
		"Content-Type":"application/json",
		"Origin":"https://127.0.0.1:" +info.port,
		"Sec-Fetch-Dest":"empty",
		"Sec-Fetch-Mode":"cors",
		"Sec-Fetch-Site":"same-origin",
		"Sec-Fetch-User":" ?F",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) RiotClient/" + info.version + " (CEF 74) Safari/537.36",
		"sec-ch-ua":"Chromium",
		"Referer":"https://127.0.0.1:" + info.port + "/index.html",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"en-US,en;q=0.9"
        }

__ENDPOINTS = {
    "skins" : "https://127.0.0.1/lol-inventory/v2/inventory/CHAMPION_SKIN",
    "champion_select" : "https://127.0.0.1/lol-champ-select/v1/session",
    "player": "https://127.0.0.1/lol-summoner/v1/summoners/",
    "ranked_select" : "https://127.0.0.1/chat/v5/participants/champ-select",
}

def endpoint(select, port, player_id=None):
    endpoint_ = __ENDPOINTS[select][:17] + ":" + str(port) + __ENDPOINTS[select][17:]
    if select =="player":
        endpoint_ += str(player_id)
    return endpoint_

class Connection:
    @staticmethod
    def request(url, headers):
        context = ssl.SSLContext() #https zzz
        url_ = urllib.request.Request(url=url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(url_, context=context) as fd:
                return fd.read()
        except Exception as e:
            return f"Error when requesting resource:\n\tError: {e.msg}"
