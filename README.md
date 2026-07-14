# Voice Assistant Project 🎤

## Overview
This project is a Python-based voice assistant that listens to spoken commands and responds with useful actions.  
It supports both beginner and advanced features, including NLP, email, reminders, and weather updates.

---

## Features
### Beginner Tier
- Capture voice input using `speech_recognition`
- Respond to "Hello" with a greeting
- Tell the current time and date
- Perform a web search
- Error handling for unrecognized input
- Text-to-speech feedback using `pyttsx3`

### Advanced Tier
- Natural language understanding (NLP with `transformers`)
- Send emails via voice command (`smtplib`)
- Set reminders with audible alerts
- Fetch live weather updates (OpenWeatherMap API)
- Answer general knowledge questions (QA API)
- Custom commands via `commands.json`
- Privacy considerations documented

---

## Tech Stack
- Python 3
- Libraries: `speech_recognition`, `pyttsx3`, `requests`, `transformers`, `smtplib`
- Optional: `pyaudio` for microphone input

---

## Installation
```bash
pip install speechrecognition pyttsx3 requests transformers pyaudio
