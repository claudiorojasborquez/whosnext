import psutil 
import base64
import internals
import re

class ClientInfo:
    def __init__(self, riot_client=False):
        self.__cmdline = None
        self.riot_client = riot_client

    def __get_pids(self) -> dict[int, str]:
        return {
        p.info["pid"]: p.info["name"]
        for p in psutil.process_iter(attrs=["pid", "name"])
        }
    
    @property
    def league_pid(self) -> int:
        pids = self.__get_pids()
        try:
            return list(pids.keys())[list(pids.values()).index("LeagueClientUx.exe")]
        except ValueError:
            raise ClientInfoError("No se encuentra el cliente de LOL", code=-1)
    
    @property
    def commandline(self):
        if self.__cmdline is None:
            self.__cmdline = internals.ProcessInformation(process_id=self.league_pid).command_line
        return self.__cmdline
           
    def __parse_token(self):
        if self.riot_client:
            pattern = r"--riotclient-auth-token=([\w-]*)"
        else:
            pattern = r"--remoting-auth-token=([\w-]*)"

        token_array = re.findall(pattern, self.commandline)
        if len(token_array) != 1:
            raise ClientInfoError(msg=f"Error when parsing token:\n\ttoken_array {token_array}")
        return token_array[0]

    @property
    def token(self) -> str:
        token_= "riot:" + self.__parse_token()
        token_= token_.encode("ascii")
        b64token = base64.b64encode(token_) 
        return str(b64token.decode("utf-8"))
    
    @property
    def version(self) -> str:
        """
        TODO: HARDCODED, this is far from being done
        """
        return "13.3.491.715"

    def __parse_port(self):
        if self.riot_client:
            pattern = r"--riotclient-app-port=([\d]*)"
        else:
            pattern = r"--app-port=([\d]*)"
        port_array = re.findall(pattern, self.commandline)
        if len(port_array) != 1:
            raise ClientInfoError(msg=f"Error when parsing port:\n\tport_array {port_array}")
        return port_array[0]
    
    @property
    def port(self) -> str:
        return self.__parse_port()
    
    def __repr__(self) -> str:
        return f"""
        Client information:
            pid: {self.league_pid}
            port: {self.port}
            token: {self.token}
            version: {self.version}
            command line: {self.commandline}
        """

class ClientInfoError(Exception):
    def __init__(self, *args, code="", **kwargs):
        self.code = code
        super().__init__(args, kwargs)

if __name__=="__main__":
    info = ClientInfo()
    print(info)
