# 🖼️ Discord Image Logger

**A powerful, open-source tool for educational and research purposes that demonstrates how Discord's "Open Original" feature can be exploited to gather IP addresses and system information.**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-red)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

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
