# 🖼️ Discord Image Logger | Tim$erz

**A powerful, open-source tool for educational and research purposes that demonstrates how Discord's "Open Original" feature can be exploited to gather IP addresses and system information.**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-red)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

---

## ⚠️ DISCLAIMER - READ THIS FIRST

> **🚨 IMPORTANT: This tool is provided SOLELY FOR EDUCATIONAL AND RESEARCH PURPOSES.**
>
> **⛔ YOU ARE NOT ALLOWED TO:**
> - ❌ Use this tool for malicious purposes
> - ❌ Use this tool without explicit consent from all parties involved
> - ❌ Violate Discord's Terms of Service
> - ❌ Share, sell, or distribute collected data
> - ❌ Target individuals without their knowledge
> - ❌ Use this for harassment, doxxing, or any illegal activity
>
> **✅ YOU ARE ALLOWED TO:**
> - ✔️ Use this in controlled, consensual environments
> - ✔️ Educate others about privacy and security risks
> - ✔️ Test your own systems and networks
> - ✔️ Report security vulnerabilities responsibly
> - ✔️ Learn how web technologies work
> - ✔️ Understand how Discord's features can be exploited
>
> **👨‍⚖️ The author is NOT responsible for any misuse or damage caused by this tool.**
>
> *By downloading, installing, or using this tool, you agree to take FULL responsibility for your actions.*

---

## 📖 What is This?

**Discord Image Logger** is a Python-based HTTP server that demonstrates a privacy vulnerability in Discord's "Open Original" feature.

### 🔍 How It Works

| # | Step | Description |
|---|------|-------------|
| 1️⃣ | **Host the script** | Run on your PC, VPS, or using ngrok |
| 2️⃣ | **Get a link** | `https://your-site.com/imagelogger` |
| 3️⃣ | **Share the link** | Post in a Discord server or DM |
| 4️⃣ | **Discord fetches preview** | Shows a harmless loading image |
| 5️⃣ | **User clicks "Open Original"** | Their browser loads the image |
| 6️⃣ | **Information is logged** | IP, location, browser, OS, etc. |
| 7️⃣ | **Data sent to Discord** | Delivered via your webhook |

### 🎯 Why This Matters

Discord's "Open Original" feature is designed to let users view the original version of an image. However, when a user clicks this, their browser makes a direct request to the server hosting the image. This request reveals their IP address, user agent, and other information. This is not a Discord-specific issue - it's how the internet works. The purpose of this tool is to educate people about these privacy risks.

---

## ⚡ Features

| 🏷️ Feature | 📝 Description |
|------------|----------------|
| 🌐 **IP Address Logging** | Captures the user's public IP address |
| 📍 **Geolocation** | Shows country, region, city, and approximate coordinates |
| 📡 **Precise GPS Location** | Can request the user's exact GPS location (asks for permission) |
| 💻 **User-Agent Parsing** | Identifies Operating System, Browser name, and version |
| 🛡️ **VPN/Proxy Detection** | Detects if the user is hiding their IP with a VPN or proxy |
| 🤖 **Bot Detection** | Identifies automated bots and can ignore them |
| 🖼️ **Custom Image Preview** | Use any image as the preview shown in Discord |
| 💥 **Browser Crash** | Optional browser freeze/crash for testing purposes |
| 🔄 **Custom Redirect** | Redirect users to any webpage after opening the link |
| 💬 **Custom Messages** | Display personalized messages to users |
| 🔔 **Link Share Alerts** | Get notified when someone shares your link in a chat |
| 📨 **Discord Webhook** | All data is sent directly to your Discord channel |
| 🛡️ **Anti-Bot Protection** | Prevents bots from triggering false alerts |
| 🛡️ **Anti-VPN Protection** | Can ignore or flag VPN users |

---

## 🔧 Installation

### 📋 What You Need Before Starting

| ✅ Item | ℹ️ Description |
|---------|----------------|
| 🐍 Python 3.6+ | Installed on your computer |
| 🎮 Discord Account | A server/channel you control |
| 🔗 Discord Webhook URL | Created from your Discord server settings |
| 🖥️ Command Line | Basic knowledge of terminal/command prompt |
| 🌐 (Optional) ngrok or VPS | To expose your server to the internet |

### 📥 Step 1: Get the Code

Open your terminal/command prompt and run:

```bash
git clone https://github.com/your-username/Discord-Image-Logger.git
cd Discord-Image-Logger
```

> 💡 **Tip:** If you don't have Git installed, download the ZIP file from GitHub and extract it.

### 📦 Step 2: Install Required Python Libraries

```bash
pip install requests
pip install httpagentparser
```

Or install both at once:

```bash
pip install requests httpagentparser
```

### 🔗 Step 3: Create a Discord Webhook

| # | Action |
|---|--------|
| 1️⃣ | Open Discord and go to your server/channel |
| 2️⃣ | Click the gear icon (Server Settings) |
| 3️⃣ | Click on **"Integrations"** in the left sidebar |
| 4️⃣ | Click on **"Webhooks"** |
| 5️⃣ | Click **"New Webhook"** |
| 6️⃣ | Give it a name (e.g., "Image Logger") |
| 7️⃣ | Click **"Copy Webhook URL"** |

> ⚠️ **Warning:** Keep your webhook URL secret! Anyone with it can receive your logs.

### ⚙️ Step 4: Configure the Script

Open `main.py` in a text editor and set:

```python
config = {
    "webhook": "YOUR_WEBHOOK_URL_HERE",  # 🔴 REQUIRED
    "image": "https://example.com/your-image.png",  # Optional
    "username": "Image Logger",  # Webhook display name
    "color": 0x00FFFF,  # Embed color
}
```

### 🚀 Step 5: Run the Server

```bash
python main.py
```

You should see:
```
Serving HTTP on :: port 8080 ...
```

Your server is running on `http://localhost:8080`

### 🌍 Step 6: Expose to the Internet (Optional)

**Option A: Using ngrok (Easiest for Testing)**

```bash
ngrok http 8080
```

You'll get a URL like: `https://abc123.ngrok.io`

**Option B: Using a VPS (Permanent Hosting)**

```bash
sudo ufw allow 8080
```

Access at: `https://your-vps-ip.com:8080/imagelogger`

---

## 🚀 Usage

### 📝 Basic Usage

| # | Step |
|---|------|
| 1️⃣ | `python main.py` |
| 2️⃣ | Get your link: `http://localhost:8080/imagelogger` |
| 3️⃣ | Share the link in Discord |
| 4️⃣ | Wait for someone to click "Open Original" |
| 5️⃣ | Check your Discord webhook channel |

### 🔗 URL Arguments (Advanced)

| Argument | What It Does | Example |
|----------|--------------|---------|
| `?url=` | Custom image (base64 encoded) | `?url=aHR0cHM6Ly9leGFtcGxlLmNvbS9pbWFnZS5wbmc=` |
| `?id=` | Same as `url`, alternative | `?id=aHR0cHM6Ly9leGFtcGxlLmNvbS9pbWFnZS5wbmc=` |
| `?g=` | GPS coordinates (auto-added) | `?g=MzcsLTEyMg==` |

### 📌 Example Full URL

```
https://your-domain.com/imagelogger?url=aHR0cHM6Ly9leGFtcGxlLmNvbS9pbWFnZS5wbmc=
```

---

## ⚙️ Configuration

### 🔧 Complete Configuration Options

| Setting | Type | Description | Default |
|---------|------|-------------|---------|
| `webhook` | string | Discord webhook URL (**REQUIRED**) | `""` |
| `image` | string | Image URL for "Open Original" | `""` |
| `imageArgument` | boolean | Allow URL arguments | `True` |
| `username` | string | Webhook display name | `"Image Logger"` |
| `color` | hex | Embed color | `0x00FFFF` |
| `crashBrowser` | boolean | Attempt to crash browser | `False` |
| `accurateLocation` | boolean | Request GPS location | `False` |
| `message.doMessage` | boolean | Show custom message | `False` |
| `message.message` | string | Custom message text | `"..."` |
| `message.richMessage` | boolean | Enable placeholders | `True` |
| `vpnCheck` | integer | VPN detection level | `1` |
| `linkAlerts` | boolean | Alert on link share | `True` |
| `buggedImage` | boolean | Show loading image preview | `True` |
| `antiBot` | integer | Bot detection level | `1` |
| `redirect.redirect` | boolean | Redirect to another page | `False` |
| `redirect.page` | string | Redirect URL | `"https://your-link.here"` |

### 🛡️ VPN/Proxy Detection Levels

| Level | Behavior |
|-------|----------|
| `0` | 🌍 No anti-VPN - logs everyone |
| `1` | ⚠️ Don't ping @everyone when VPN suspected |
| `2` | 🚫 Don't send any alert when VPN suspected |

### 🤖 Anti-Bot Detection Levels

| Level | Behavior |
|-------|----------|
| `0` | 🤖 No anti-bot - logs everything |
| `1` | ⚠️ Don't ping when possibly a bot |
| `2` | ⚠️ Don't ping when 100% a bot |
| `3` | 🚫 Don't send alert when possibly a bot |
| `4` | 🚫 Don't send alert when 100% a bot |

### 📝 Message Placeholders (Rich Message)

| Placeholder | Replaces With |
|-------------|---------------|
| `{ip}` | User's IP address |
| `{isp}` | Internet Service Provider |
| `{asn}` | Autonomous System Number |
| `{country}` | Country name |
| `{region}` | Region/State name |
| `{city}` | City name |
| `{lat}` | Latitude coordinate |
| `{long}` | Longitude coordinate |
| `{timezone}` | Timezone |
| `{mobile}` | Mobile device status |
| `{vpn}` | VPN detected? |
| `{bot}` | Bot detected? |
| `{browser}` | Browser name/version |
| `{os}` | Operating system |

**Example message:**

```
Hello {ip}! Your ISP is {isp} and you're located in {city}, {country}. You are using {browser} on {os}. This is for educational purposes only!
```

---

## 📊 Data Collected

### 🌐 IP Information

| Data | Description |
|------|-------------|
| 📍 IP Address | User's public IP |
| 🏢 ISP | Internet Service Provider |
| 🔢 ASN | Autonomous System Number |
| 🌍 Country | Country of origin |
| 🗺️ Region | Region/State |
| 🏙️ City | City name |
| 📌 Coordinates | Approximate latitude/longitude |
| 🕐 Timezone | IP location timezone |

### 💻 Device Information

| Data | Description |
|------|-------------|
| 🖥️ Operating System | OS name and version |
| 🌐 Browser | Browser name and version |
| 📄 User Agent | Full user-agent string |

### 🌐 Network Information

| Data | Description |
|------|-------------|
| 🛡️ VPN/Proxy | Detected VPN or proxy |
| 📱 Mobile | Mobile device detected |
| 🤖 Bot | Automated bot detected |

### 📨 Example Webhook Output

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

## 🛡️ Privacy & Security

### ⚖️ Legal Guidelines

> **📚 This tool is intended for educational purposes only.**

| ✅ DO | ❌ DON'T |
|-------|----------|
| Obtain explicit consent | Use without consent |
| Educate about privacy | Share or misuse data |
| Test in controlled environments | Target individuals |
| Report vulnerabilities | Violate Discord ToS |

### 🔒 Where the Data Goes

| Destination | Status |
|-------------|--------|
| Discord Webhook | ✅ Only destination |
| Server Storage | ❌ Not stored |
| Third Parties | ❌ Not shared |
| Log Files | ❌ Not logged |

### 🛡️ Protecting Yourself

| Action | Why |
|--------|-----|
| 🔐 Keep webhook URL secret | Anyone with it can receive your data |
| 🔒 Use HTTPS | Encrypts traffic |
| 📁 Don't share logs | Contains sensitive information |
| 🗑️ Delete old webhooks | Prevents unauthorized access |

---

## 🐞 Troubleshooting

### 🔧 Common Issues and Fixes

| ❌ Issue | ✅ Solution |
|----------|-------------|
| ModuleNotFoundError: 'requests' | Run `pip install requests` |
| ModuleNotFoundError: 'httpagentparser' | Run `pip install httpagentparser` |
| Webhook not sending | Check webhook URL is correct |
| No data when testing | Click "Open Original" |
| Server won't start | Port 8080 in use - change port |
| ngrok not working | Install ngrok and create account |
| Firewall blocking | Allow port 8080 |
| Bot detection blocking | Adjust `antiBot` settings |
| VPN detection blocking | Adjust `vpnCheck` settings |

### 🔢 Error Codes

| Code | Meaning |
|------|---------|
| 200 | ✅ OK - Request successful |
| 302 | 🔄 Redirect - User redirected |
| 500 | ❌ Internal Server Error |

---

## 📝 License

This project is licensed under the **MIT License**.

| ✅ Allowed | ⚠️ Required |
|------------|-------------|
| Use for any purpose | Include copyright notice |
| Modify the code | Include license text |
| Distribute copies | Provide warranty disclaimer |

**This software is provided "AS IS" without warranty of any kind.**

---

## 👨‍💻 Author

**Timzz71**

| Platform | Handle |
|----------|--------|
| 🐦 GitHub | github.com/timzz71 |
| 🎮 Discord | `Crypted3057` (ID: `884763850749120544`) |
| 📧 Email | timcrypted3057@gmail.com |

---

## ⭐ Support

If you find this tool useful for educational purposes:

| Action | Why |
|--------|-----|
| ⭐ Star the repository | Shows appreciation |
| 🐛 Report issues | Helps improve the tool |
| 🔧 Submit pull requests | Contribute code |
| 📚 Share this | Educate others about privacy |

---

## 📌 Final Notes

**🔬 This tool is a demonstration of how browser-based tracking works. The purpose is EDUCATION, not exploitation.**

The internet is not anonymous. Every time you click a link, you reveal information about yourself. This tool shows you what information is exposed and why you should be careful about what links you click.

**🧠 Use this knowledge responsibly.**

---

*Made with ❤️ for educational purposes*

**📅 Last Updated:** 28/08/2026
