# 🤖 JARVIS — Personal AI Assistant

**A Cross-Platform Voice-Controlled AI Assistant** — By Dilip

A real-time voice AI that can hear, see, understand, and control your computer. Built to bring a JARVIS-style experience to your everyday workflow — automating tasks, monitoring your system, and acting as a proactive digital companion.

---

## ✨ Overview

JARVIS is a personal AI assistant that bridges the gap between your operating system, real-time web intelligence, and everyday productivity tools. Through natural dialogue, it can control your desktop, browse the web, manage files, monitor system health, and remember context across sessions.

It's not just a chatbot — it's an extension of your digital life.

---

## 🚀 Capabilities

| Feature | Description |
|---|---|
| 🎙️ **Voice Interaction** | Speech-to-text and text-to-speech for natural conversation |
| 🖥️ **System Control** | Launch apps, manage files, execute terminal commands |
| 🌐 **Browser Control** | Automate and control web browsing tasks |
| 👁️ **Screen Awareness** | Real-time screen processing and analysis |
| 🧠 **Persistent Memory** | Remembers your preferences, projects, and personal context |
| 📊 **System Monitoring** | Tracks CPU, RAM, and other system metrics |
| 🔍 **Web Search** | Built-in web search and research capabilities |
| ⏰ **Reminders** | Set and manage reminders and scheduled tasks |
| 🌦️ **Weather Reports** | Get local weather updates on request |
| ✈️ **Flight Finder** | Search for flight information |
| 🎮 **Game Updater** | Keep your games up to date |
| 📺 **YouTube Integration** | Search and interact with YouTube content |
| 💻 **Code Helper & Dev Agent** | Assistance with coding and development tasks |
| 📊 **Dashboard** | Web-based dashboard for monitoring and control |

---

## ⚡ Quick Start

```bash
git clone https://github.com/Dilip2557/personal-assistence-jarvis.ai.git
cd personal-assistence-jarvis.ai
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

> **Installation Note:** If you run into a `ModuleNotFoundError`, install the missing package via `pip install <module_name>` for your specific system.

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.11 or later |
| **Microphone** | Required for voice interaction |
| **API Key** | LLM provider API key (see `config/` setup) |

---

## 🔐 Configuration

Before running JARVIS, set up your API keys and certificates locally:

```bash
cp config/api_keys.example.json config/api_keys.json
# Fill in your API key(s)
```

> ⚠️ **Never commit `config/api_keys.json` or files in `config/certs/` to version control.** These are ignored via `.gitignore` and should stay local to your machine.

---

## 🛠️ Project Structure

```
jarvis/
├── actions/        # Individual assistant capabilities (browser, files, weather, etc.)
├── config/         # API keys and certificates (local only)
├── core/           # LLM client, STT/TTS, installer
├── dashboard/      # Web dashboard server + static UI
├── memory/         # Persistent memory management
├── main.py         # Entry point
└── ui.py           # Assistant UI
```

---

## ⚠️ License

Personal and non-commercial use only.

---

## 👤 Author

Built by **Dilip** — a personal project exploring real-world JARVIS-style AI assistants.

⭐ Star the repository if you find it useful!
