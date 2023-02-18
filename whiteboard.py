import re
import base64

cmdline = """ "C:/Riot Games/League of Legends/LeagueClientUx.exe" "--riotclient-auth-token=14R2r5MAle51-N6geoDREw" "--riotclient-app-port=5676--riotgamesapi-standalone" "--riotgamesapi-settings=eyJjbGllbnQtY29uZmlnJzZXNzaW9uLWlkIjoiZDNmNTBjMjgtOTFlNi03MTQ1LWEzYTQtZTA4MTJkYmJkNjkwIn0sInBhdGNobGluZV9pZCI6ImxpdmUiLCJwcm9kdWN0LWludGVncmF0aW9uIjp7ImFwcC11cGRhdGUtc3RhdHVzIjoiQzovUHJvZ3JhbURhdGEvUmlvdCBHYW1lcy9NZXRhZGF0YS9sZWFndWVfb2ZfbGVnZW5kcy5saXZlL2xlYWd1ZV9vZl9sZWdlbmRzLmxpdmUudXBkYXRlLXN0YXR1cy5qc29uIiwiaGVhcnRiZWF0IjoiQzovVXNlcnMvQ2xhdWRpby9BcHBEYXRhL0xvY2FsL1Jpb3QgR2FtZXMvUmlvdCBDbGllbnQvRGF0YS9TZXNzaW9ucy9kM2Y1MGMyOC05MWU2LTcxNDUtYTNhNC1lMDgxMmRiYmQ2OTAvMTRSMnI1TUFsZTUxLU42Z2VvRFJFdy5oZWFydGJlYXQuanNvbiIsImxvY2tmaWxlIjoiQzovUHJvZ3JhbURhdGEvUmlvdCBHYW1lcy9NZXRhZGF0YS9sZWFndWVfb2ZfbGVnZW5kcy5saXZlL2xlYWd1ZV9vZl9sZWdlbmRzLmxpdmUubG9ja2ZpbGUiLCJzZXR0aW5ncyI6IkM6L1Byb2dyYW1EYXRhL1Jpb3QgR2FtZXMvTWV0YWRhdGEvbGVhZ3VlX29mX2xlZ2VuZHMubGl2ZS9sZWFndWVfb2ZfbGVnZW5kcy5saXZlLnByb2R1Y3Rfc2V0dGluZ3MueWFtbCJ9LCJwcm9kdWN0X2lkIjoibGVhZ3VlX29mX2xlZ2VuZHMiLCJwdWJsaXNoZXIiOiJyaW90IiwicmVnaW9uX2RhdGEiOnsiTEEyIjp7ImF2YWlsYWJsZV9sb2NhbGVzIjpbImVzX01YIl0sImRlZmF1bHRfbG9jYWxlIjoiZXNfTVgiLCJyc28iOnsiY2xpZW50IjoibG9sIn19fSwicmlvdGNsaWVudCI6eyJhcHAtcG9ydCI6IjU2NzYwIiwiYXV0aC10b2tlbiI6IjE0UjJyNU1BbGU1MS1ONmdlb0RSRXcifSwicmlvdGdhbWVzYXBpIjp7InBlcnNpc3RlbmNlLXBhdGgiOiJDOi9Vc2Vycy9DbGF1ZGlvL0FwcERhdGEvTG9jYWwvUmlvdCBHYW1lcy9MZWFndWUgb2YgTGVnZW5kcyJ9LCJyc29fYXV0aCI6eyJhdXRob3JpemF0aW9uLWtleSI6ImV3MEtJQ0FnSUNKamIyUmxJam9nSW1SWVkzaFBia3BWVGxSV05HSjZSbmxWTTAweFVsUmtWbFpYVmtSVk1IUkVXV3hGZFZZeVpIWk5NbFpzVmtaa2JscFZVbmRUTWpGVlpXMW9NV1JyV2pWa2R6MDlJaXdOQ2lBZ0lDQWlZMjlrWlY5MlpYSnBabWxsY2lJNklDSldiak5VVVhkdWQwMTZSRlZvUWtWWE5XbFNVMUpZU1c0MVZEWmtXRFJWVjBjdFQycERWR0l0VEZkSk4yRm1RbWxKVUZkZlkxWXpla1ZOZWpOd2RVRXRiemt3U0RCaFl5MDBRVlp0ZWw5bWEwZHpiMlJSVVNJTkNuMD0ifX0=" "--rga-lite" "--remoting-auth-token=9y493gDaMx06wba0sV-xZw" "--respawn-command=LeagueClient.exe" "--respawn-display-name=League of Legends" "--app-port=56880" "--install-directory=C:\Riot Games\League of Legends" "--app-name=LeagueClient" "--ux-name=LeagueClientUx" "--ux-helper-name=LeagueClientUxHelper" "--log-dir=LeagueClient Logs" "--crash-reporting=crashpad" "--crash-environment=LA2" "--crash-pipe=\\.\pipe\crashpad_24860_ZEOBLNDRXBLGWWWN" "--app-log-file-path=C:/Riot Games/League of Legends/Logs/LeagueClient Logs/2023-02-17T01-37-56_24860_LeagueClient.log" "--app-pid=24860" "--output-base-dir=C:\Riot Games\League of Legends" "--no-proxy-server" "--ignore-certificate-errors" """

token_re = r"--remoting-auth-token=([\w-]*)"
pattern = re.compile(token_re)
token = pattern.findall(cmdline)[0]

def token(token_) -> str:
    token_= "riot:" + token_
    token_= token_.encode("ascii")
    b64token = base64.b64encode(token_) 
    return str(b64token.decode("utf-8"))

print(token)
