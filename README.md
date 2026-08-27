# 🖼️ Discord Image Logger

```
████████╗██╗███╗░░░███╗███████╗██████╗░███████╗██████╗░███████╗
╚══██╔══╝██║████╗░████║██╔════╝██╔══██╗╚════██║╚════██╗╚════██║
░░░██║░░░██║██╔████╔██║█████╗░░██████╔╝░░███╔═╝░█████╔╝░░███╔═╝
░░░██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══╝░░██╔═══╝░██╔══╝░░
░░░██║░░░██║██║░╚═╝░██║███████╗██║░░██║███████╗██║░░░░░███████╗
░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚══════╝
```
```
  ███████╗███████╗██████╗░  ██████╗░██████╗░██╗██╗░░░██╗███████╗
  ██╔════╝╚════██║╚════██╗  ██╔══██╗╚════██╗██║██║░░░██║╚════██║
  █████╗░░░░███╔═╝░█████╔╝  ██████╦╝░█████╔╝██║╚██╗░██╔╝░░███╔═╝
  ██╔══╝░░██╔══╝░░░╚═══██╗  ██╔══██╗░╚═══██╗██║░╚████╔╝░██╔══╝░░
  ██║░░░░░███████╗██████╔╝  ██████╦╝██████╔╝██║░░╚██╔╝░░███████╗
  ╚═╝░░░░░╚══════╝╚═════╝░  ╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░╚══════╝
```

**A powerful, open-source tool for educational and research purposes that demonstrates how Discord's "Open Original" feature can be exploited to gather IP addresses and system information.**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-red)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

---

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                  🄲🅁🄴🄰🅃🄴🄳 🄱🅈 🅃🄸🄼$🄴🅁🅉                        │
│                                                             │
│     ████████╗██╗███╗░░░███╗███████╗███████╗██████╗        │
│     ╚══██╔══╝██║████╗░████║╚════██║╚════██║╚════██╗       │
│     ░░░██║░░░██║██╔████╔██║░░███╔═╝░░███╔═╝░█████╔╝       │
│     ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══╝░░██╔═══╝        │
│     ░░░██║░░░██║██║░╚═╝░██║███████╗███████╗██║░░░░░        │
│     ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░░░░        │
│                                                             │
│                 🄶🄸🅃🄷🅄🄱: @🅃🄸🄼🅉🄯71                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ DISCLAIMER - READ THIS FIRST

> **IMPORTANT: This tool is provided SOLELY FOR EDUCATIONAL AND RESEARCH PURPOSES.**
>
> **YOU ARE NOT ALLOWED TO:**
> - ❌ Use this tool for malicious purposes
> - ❌ Use this tool without explicit consent from all parties involved
> - ❌ Violate Discord's Terms of Service
> - ❌ Share, sell, or distribute collected data
> - ❌ Target individuals without their knowledge
> - ❌ Use this for harassment, doxxing, or any illegal activity
>
> **YOU ARE ALLOWED TO:**
> - ✅ Use this in controlled, consensual environments
> - ✅ Educate others about privacy and security risks
> - ✅ Test your own systems and networks
> - ✅ Report security vulnerabilities responsibly
> - ✅ Learn how web technologies work
> - ✅ Understand how Discord's features can be exploited
>
> **The author is NOT responsible for any misuse or damage caused by this tool.**
>
> *By downloading, installing, or using this tool, you agree to take FULL responsibility for your actions.*

---

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           ⚡ DEVELOPED BY Tim$erz ⚡                      ║
║                                                           ║
║   ███████╗██╗   ██╗██╗     ██╗      ███████╗██████╗     ║
║   ██╔════╝╚██╗ ██╔╝██║     ██║      ██╔════╝╚════██╗    ║
║   █████╗   ╚████╔╝ ██║     ██║█████╗███████╗ █████╔╝    ║
║   ██╔══╝    ╚██╔╝  ██║     ██║╚════╝╚════██║██╔═══╝     ║
║   ███████╗   ██║   ███████╗███████╗███████║███████╗     ║
║   ╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 📖 What is This?

**Discord Image Logger** is a Python-based HTTP server that demonstrates a privacy vulnerability in Discord's "Open Original" feature.

### How It Works (Simple Explanation)

1. **You host this script** on a server (your PC, a VPS, or using ngrok)
2. **You get a link** like `https://your-site.com/imagelogger`
3. **You share the link** in a Discord server or direct message
4. **Discord fetches a preview** - it sees a loading image (not suspicious)
5. **A user clicks "Open Original"** to see the full image
6. **Their information is logged** - IP address, location, browser, OS, etc.
7. **Data is sent to your Discord channel** via a webhook

### Why This Matters

Discord's "Open Original" feature is designed to let users view the original version of an image. However, when a user clicks this, their browser makes a direct request to the server hosting the image. This request reveals their IP address, user agent, and other information. This is not a Discord-specific issue - it's how the internet works. The purpose of this tool is to educate people about these privacy risks.

---

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                  🄲🅁🄴🄰🅃🄾🅁: 🅃🄸🄼$🄴🅁🅉                            │
│                                                             │
│              ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗  │
│             ██╔════╝ ██║╚══██╔══╝██║  ██║╚██╗ ██╔╝╚════██╗ │
│             ██║  ███╗██║   ██║   ███████║ ╚████╔╝  █████╔╝ │
│             ██║   ██║██║   ██║   ██╔══██║  ╚██╔╝  ██╔═══╝  │
│             ╚██████╔╝██║   ██║   ██║  ██║   ██║   ███████╗ │
│              ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝ │
│                                                             │
│              🄶🄸🅃🄷🅄🄱: 🄶🄸🅃🄷🅄🄱.🄲🄾🄼/🅃🄸🄼🅉🄯71                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| **IP Address Logging** | Captures the user's public IP address |
| **Geolocation** | Shows country, region, city, and approximate coordinates |
| **Precise GPS Location** | Can request the user's exact GPS location (asks for permission) |
| **User-Agent Parsing** | Identifies Operating System, Browser name, and version |
| **VPN/Proxy Detection** | Detects if the user is hiding their IP with a VPN or proxy |
| **Bot Detection** | Identifies automated bots and can ignore them |
| **Custom Image Preview** | Use any image as the preview shown in Discord |
| **Browser Crash** | Optional browser freeze/crash for testing purposes |
| **Custom Redirect** | Redirect users to any webpage after opening the link |
| **Custom Messages** | Display personalized messages to users |
| **Link Share Alerts** | Get notified when someone shares your link in a chat |
| **Discord Webhook** | All data is sent directly to your Discord channel |
| **Anti-Bot Protection** | Prevents bots from triggering false alerts |
| **Anti-VPN Protection** | Can ignore or flag VPN users |

---

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                 🌟 CODED BY Tim$erz 🌟                    ║
║                                                           ║
║           🔗 https://github.com/timzz71 🔗               ║
║                                                           ║
║   ▄▀▀▄ █▀▀▄ █▀▀▄ █▀▀ ▄▀▀▄ ▀█▀ █▀▀▄ █▀▀ ▄▀▀▄ █▀▀▄ █▀▀▀ ▄▀▀▄ ║
║   █  █ █  █ █  █ █   █  █  █  █  █ █   █  █ █  █ █    █  █ ║
║   ▀▀▀▀ ▀  ▀ ▀  ▀ ▀▀▀ ▀▀▀▀  ▀  ▀  ▀ ▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀▀ ▀▀▀▀ ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🔧 Installation

### What You Need Before Starting

- Python 3.6 or higher installed on your computer
- A Discord account and a server/channel you control
- A Discord Webhook URL (explained below)
- Basic knowledge of using the command line/terminal
- (Optional) A VPS or ngrok account to expose your server to the internet

### Step 1: Get the Code

Open your terminal/command prompt and run:

```bash
git clone https://github.com/your-username/Discord-Image-Logger.git
cd Discord-Image-Logger
```

If you don't have Git installed, you can download the ZIP file from GitHub and extract it.

### Step 2: Install Required Python Libraries

```bash
pip install requests
pip install httpagentparser
```

Or install both at once:

```bash
pip install requests httpagentparser
```

### Step 3: Create a Discord Webhook

1. Open Discord and go to the server/channel you want to receive the logs
2. Click the gear icon (Server Settings) or the channel settings
3. Click on **"Integrations"** in the left sidebar
4. Click on **"Webhooks"**
5. Click **"New Webhook"**
6. Give it a name (e.g., "Image Logger")
7. Click **"Copy Webhook URL"** - this is the URL you'll put in the config

### Step 4: Configure the Script

Open the `main.py` file in a text editor (Notepad, VS Code, etc.)

Find the `config` section and set:

```python
config = {
    "webhook": "YOUR_WEBHOOK_URL_HERE",  # Paste your Discord webhook URL here
    "image": "https://example.com/your-image.png",  # Optional custom image URL
    "username": "Image Logger",  # Name that appears on the webhook
    "color": 0x00FFFF,  # Embed color (hex value)
    # ... other settings
}
```

### Step 5: Run the Server

```bash
python main.py
```

You should see:
```
Serving HTTP on :: port 8080 ...
```

Your server is now running on `http://localhost:8080`

### Step 6: Expose to the Internet (Optional)

**Option A: Using ngrok (Easiest for Testing)**

1. Download ngrok from: https://ngrok.com/download
2. Extract the file and run:
   ```bash
   ngrok http 8080
   ```
3. You'll get a URL like: `https://abc123.ngrok.io`
4. Your full link is: `https://abc123.ngrok.io/imagelogger`

**Option B: Using a VPS (Permanent Hosting)**

1. Upload the script to your VPS
2. Install Python and dependencies
3. Run the script
4. Make sure port 8080 is open in your firewall:
   ```bash
   sudo ufw allow 8080
   ```
5. Access it at: `https://your-vps-ip.com:8080/imagelogger`

---

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│           🄲🄾🄳🄴🄳 🄱🅈 🅃🄸🄼$🄴🅁🅉  🄲🄾🄿🅈🅁🄸🄶🄷🅃 2024               │
│                                                             │
│         ████████╗██╗███╗░░░███╗███████╗███████╗██████╗    │
│         ╚══██╔══╝██║████╗░████║╚════██║╚════██║╚════██╗   │
│         ░░░██║░░░██║██╔████╔██║░░███╔═╝░░███╔═╝░█████╔╝   │
│         ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══╝░░██╔═══╝    │
│         ░░░██║░░░██║██║░╚═╝░██║███████╗███████╗██║░░░░░    │
│         ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░░░░    │
│                                                             │
│               🄶🄸🅃🄷🅄🄱: 🄶🄸🅃🄷🅄🄱.🄲🄾🄼/🅃🄸🄼🅉🄯71                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Configuration

### Complete Configuration Options

Here is every setting you can change in the `config` section:

| Setting | Type | Description | Default |
|---------|------|-------------|---------|
| `webhook` | string | Your Discord webhook URL (REQUIRED) | `""` |
| `image` | string | URL of the image shown when users click "Open Original" | `""` |
| `imageArgument` | boolean | Allow URL arguments to change the image | `True` |
| `username` | string | Name displayed on the webhook | `"Image Logger"` |
| `color` | hex | Color of the embed (hex value) | `0x00FFFF` |
| `crashBrowser` | boolean | Attempt to crash/freeze the user's browser | `False` |
| `accurateLocation` | boolean | Request GPS location (asks for permission) | `False` |
| `message.doMessage` | boolean | Show a custom message to the user | `False` |
| `message.message` | string | The custom message to show | `"..."` |
| `message.richMessage` | boolean | Enable placeholders in the message | `True` |
| `vpnCheck` | integer | VPN detection level (0, 1, or 2) | `1` |
| `linkAlerts` | boolean | Alert when someone sends the link | `True` |
| `buggedImage` | boolean | Show loading image in Discord preview | `True` |
| `antiBot` | integer | Bot detection level (0, 1, 2, 3, or 4) | `1` |
| `redirect.redirect` | boolean | Redirect to another webpage | `False` |
| `redirect.page` | string | The URL to redirect to | `"https://your-link.here"` |

### VPN/Proxy Detection Levels

| Level | What It Does |
|-------|--------------|
| `0` | No anti-VPN - logs everyone |
| `1` | Don't ping @everyone when VPN is suspected |
| `2` | Don't send any alert when VPN is suspected |

### Anti-Bot Detection Levels

| Level | What It Does |
|-------|--------------|
| `0` | No anti-bot - logs everything |
| `1` | Don't ping when possibly a bot |
| `2` | Don't ping when 100% a bot |
| `3` | Don't send any alert when possibly a bot |
| `4` | Don't send any alert when 100% a bot |

### Message Placeholders (Rich Message)

If `message.richMessage` is `True`, you can use these placeholders in your custom message:

| Placeholder | What It Replaces With |
|-------------|----------------------|
| `{ip}` | The user's IP address |
| `{isp}` | Internet Service Provider |
| `{asn}` | Autonomous System Number |
| `{country}` | Country name |
| `{region}` | Region/State name |
| `{city}` | City name |
| `{lat}` | Latitude coordinate |
| `{long}` | Longitude coordinate |
| `{timezone}` | Timezone (e.g., "New York (America)") |
| `{mobile}` | Whether the user is on mobile |
| `{vpn}` | Whether a VPN was detected |
| `{bot}` | Whether a bot was detected |
| `{browser}` | Browser name and version |
| `{os}` | Operating system name |

**Example custom message:**

```
Hello {ip}! Your ISP is {isp} and you're located in {city}, {country}. You are using {browser} on {os}. This is for educational purposes only!
```

---

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              ✦ Tim$erz - GitHub ✦                       ║
║                                                           ║
║         ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗            ║
║         ║ ╔═╝║ ═ ║║ ═ ║║ ╔═╝║ ╔╗║╚═╗ ║║ ╔═╝            ║
║         ║ ╚═╗║ ═ ║║ ═ ║║ ╚═╗║ ╚╝║ ╔╝╔╝║ ╚═╗            ║
║         ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝ ╚══╝ ╚═══╝            ║
║                                                           ║
║              🄶🄸🅃🄷🅄🄱: 🄶🄸🅃🄷🅄🄱.🄲🄾🄼/🅃🄸🄼🅉🄯71                   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 📊 Data Collected

When a user clicks "Open Original", the following data is logged and sent to your Discord webhook:

### IP Information

| Data | Description |
|------|-------------|
| **IP Address** | The user's public IP address |
| **ISP** | Internet Service Provider name |
| **ASN** | Autonomous System Number |
| **Country** | Country where the IP is registered |
| **Region** | Region/State name |
| **City** | City name |
| **Coordinates** | Approximate latitude and longitude |
| **Timezone** | Timezone of the IP location |

### Device Information

| Data | Description |
|------|-------------|
| **Operating System** | OS name and version |
| **Browser** | Browser name and version |
| **User Agent** | Full user-agent string (contains all above) |

### Network Information

| Data | Description |
|------|-------------|
| **VPN/Proxy** | Whether a VPN or proxy was detected |
| **Mobile** | Whether the user is on a mobile device |
| **Bot** | Whether a bot was detected |

### Example of What You'll Receive

```
📡 Image Logger - IP Logged

Endpoint: /imagelogger

IP Info:
> IP: 192.168.1.1
> Provider: Google LLC
> ASN: AS15169
> Country: United States
> Region: California
> City: Mountain View
> Coords: 37.422, -122.084
> VPN: False
> Bot: False

PC Info:
> OS: Windows 10
> Browser: Chrome 120

User Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...
```

---

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│            🄿🅁🄾🄹🄴🄲🅃 🄱🅈 🅃🄸🄼$🄴🅁🅉 - 🄲🅁🄴🄰🅃🄾🅁                 │
│                                                             │
│         ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗      │
│        ██╔════╝ ██║╚══██╔══╝██║  ██║╚██╗ ██╔╝╚════██╗     │
│        ██║  ███╗██║   ██║   ███████║ ╚████╔╝  █████╔╝     │
│        ██║   ██║██║   ██║   ██╔══██║  ╚██╔╝  ██╔═══╝      │
│        ╚██████╔╝██║   ██║   ██║  ██║   ██║   ███████╗     │
│         ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝     │
│                                                             │
│              🄶🄸🅃🄷🅄🄱: 🄶🄸🅃🄷🅄🄱.🄲🄾🄼/🅃🄸🄼🅉🄯71                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Privacy & Security

### Legal Guidelines

**This tool is intended for educational purposes only. Before using it, consider:**

1. **Obtain explicit consent** from all parties you plan to log
2. **Never share or misuse** the data you collect
3. **Respect user privacy** - comply with GDPR, CCPA, and your local laws
4. **Use for education** - teach others about privacy risks
5. **Don't target individuals** without their knowledge and consent
6. **Don't violate Discord's Terms of Service**

### Where the Data Goes

- Data is sent **ONLY** to your Discord webhook
- No data is stored on the server
- No data is sent to third parties
- No data is logged to files (unless you modify the script)

### Protecting Yourself

- **Keep your webhook URL secret** - anyone with it can receive your data
- **Use HTTPS** when possible to encrypt traffic
- **Don't share logs publicly** - they contain sensitive information
- **Delete old webhooks** when you're done testing

### Your Responsibility

By using this tool, you agree that:

1. You will not use it for malicious purposes
2. You will not target anyone without their consent
3. You are solely responsible for your actions
4. The author is not liable for any misuse

---

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                 🄲🅁🄴🄰🅃🄾🅁: 🅃🄸🄼$🄴🅁🅉                               ║
║                                                           ║
║                   ╔═══╗╔═══╗╔═══╗╔═══╗                   ║
║                   ║ ╔═╝║ ═ ║║ ═ ║║ ╔═╝                   ║
║                   ║ ╚═╗║ ═ ║║ ═ ║║ ╚═╗                   ║
║                   ╚═══╝╚═══╝╚═══╝╚═══╝                   ║
║                                                           ║
║                   🄶🄸🅃🄷🅄🄱: @🅃🄸🄼🅉🄯71                            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🐞 Troubleshooting

### Common Issues and Fixes

| Issue | Solution |
|-------|----------|
| **ModuleNotFoundError: No module named 'requests'** | Run `pip install requests` |
| **ModuleNotFoundError: No module named 'httpagentparser'** | Run `pip install httpagentparser` |
| **Webhook not sending data** | Check your webhook URL is correct and active |
| **No data when testing** | Make sure you clicked "Open Original", not just viewed the preview |
| **Server won't start** | Port 8080 might be in use. Change the port in the script |
| **ngrok not working** | Make sure ngrok is installed and you have an account |
| **Firewall blocking** | Allow port 8080 in your firewall settings |
| **Bot detection blocking** | Adjust `antiBot` settings if you want to see bots |
| **VPN detection blocking** | Adjust `vpnCheck` settings if you want to see VPN users |

### Error Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request was successful |
| 302 | Redirect - User was redirected |
| 500 | Internal Server Error - Something went wrong |

### Testing Without Discord

You can test locally by:

1. Opening your browser
2. Going to `http://localhost:8080/imagelogger`
3. Check your console for logs (or Discord webhook)

---

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    ⚡ Tim$erz ⚡                            │
│                                                             │
│   ████████╗██╗███╗░░░███╗███████╗███████╗██████╗███████╗  │
│   ╚══██╔══╝██║████╗░████║╚════██║╚════██║╚════██║╚════██║ │
│   ░░░██║░░░██║██╔████╔██║░░███╔═╝░░███╔═╝░█████╔╝░░███╔═╝ │
│   ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░ │
│   ░░░██║░░░██║██║░╚═╝░██║███████╗███████╗██║░░░░░███████╗ │
│   ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝ │
│                                                             │
│              🄶🄸🅃🄷🅄🄱: 🄶🄸🅃🄷🅄🄱.🄲🄾🄼/🅃🄸🄼🅉🄯71                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**You are free to:**
- Use this software for any purpose
- Modify the code
- Distribute copies
- Include it in your own projects

**You must:**
- Include the original copyright notice
- Include the license text

**This software is provided "AS IS" without warranty of any kind.**

---

## 👨‍💻 Author

**Timzz71** (Tim$erz)

- 🐦 **GitHub:** [github.com/timzz71](https://github.com/timzz71)
- 🎮 **Discord:** `Crypted3057` (ID: `884763850749120544`)
- 📧 **Email:** `timcrypted3057@gmail.com`

---

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║            ❤️ MADE WITH LOVE BY Tim$erz ❤️               ║
║                                                           ║
║                🄶🄸🅃🄷🅄🄱: @🅃🄸🄼🅉🄯71                             ║
║                                                           ║
║         ██████╗  ██████╗ ██████╗ ███████╗               ║
║         ██╔══██╗██╔═══██╗██╔══██╗██╔════╝               ║
║         ██║  ██║██║   ██║██████╔╝█████╗                  ║
║         ██
