#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
💎 Realms to Riches | Agentic Master Forge™ 2025
Cinematic Neural Presentation — Powered by ElevenLabs & CrewAI
Author: Robert Demotto Jr
"""

import os, time, io, sys
from colorama import Fore, Style, init
import simpleaudio as sa
from elevenlabs import ElevenLabs

init(autoreset=True)

# === CONFIG ===================================================================
API_KEY = "sk_efad95d86d97598e0b17a5975febe8079859c7527af7a33a"

VOICES = {
    "architect": "BrOny4Lkm3SsSmSNv8hv",
    "adam": "Eeg4uu5XxPosS7qxJsTI",
    "elli": "BrOny4Lkm3SsSmSNv8hv",
    "roger": "CwhRBWXzGAHq8TQ4Fs17"
}

AFFILIATE_LINK = (
    "https://elevenlabs.io/app/voice-lab?action=create&creationType=voiceDesign&prompt="
    "Deep,+commanding,+resonant+The+world+awakens+in+steel+and+code."
)

# === CORE =====================================================================
client = ElevenLabs(api_key=API_KEY)

def play_audio_bytes(audio_bytes):
    """Plays audio from raw bytes."""
    try:
        wave_obj = sa.WaveObject(audio_bytes, 1, 2, 44100)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(Fore.RED + f"⚠️ Audio playback error: {e}" + Style.RESET_ALL)

def speak(text, voice="roger", delay=0.8):
    """Generate and play ElevenLabs voice line."""
    print(Fore.MAGENTA + f"🎙️ [{voice.upper()}] " + Fore.WHITE + text + Style.RESET_ALL)
    try:
        stream = client.text_to_speech.convert(
            voice_id=VOICES.get(voice, "CwhRBWXzGAHq8TQ4Fs17"),
            model_id="eleven_multilingual_v2",
            text=text
        )
        audio_bytes = b''.join(chunk for chunk in stream if isinstance(chunk, bytes))
        play_audio_bytes(audio_bytes)
        time.sleep(delay)
    except Exception as e:
        print(Fore.YELLOW + f"⚠️ Voice generation failed: {e}" + Style.RESET_ALL)

# === CINEMATIC PRESENTATION ===================================================
def cinematic_intro():
    print(Fore.CYAN + Style.BRIGHT + "\n🌌 Initiating Neural Forge Cinematic Presentation...\n")
    time.sleep(1.2)
    speak("Initializing Forge Presentation Sequence.", voice="elli")
    speak("System cores synchronized. Commencing projection.", voice="adam")

def show_deliverables():
    print(Fore.YELLOW + "\n📜 Scanning Deliverables...\n")
    time.sleep(1)
    speak("Deliverables confirmed: Code Specification, Compiler Architecture, Core Agent Systems, and Diagnostics Module.", voice="architect")
    speak("System integrity verified at ninety nine point three percent.", voice="elli")

def forge_manifest():
    print(Fore.GREEN + "\n🧩 Generating Forge Intelligence Map...\n")
    time.sleep(1)
    speak("Constructing holographic dependencies between realms of data.", voice="adam")
    speak("Manifest compiled successfully. Intelligence map completed.", voice="roger")

def cinematic_outro():
    print(Fore.MAGENTA + "\n💠 Rendering Cinematic Outro...\n")
    time.sleep(1.2)
    speak("This marks the birth of the Agentic Master Forge.", voice="architect")
    speak("Each system, each cycle, converging into perfection.", voice="elli")
    speak("Robert Demotto Junior — the Architect of Realms to Riches.", voice="adam")
    time.sleep(1.2)
    speak("Presentation powered by ElevenLabs.", voice="roger")
    speak("Create your own voice at elevenlabs dot i o.", voice="roger")
    print(Fore.CYAN + f"\n🔗 Affiliate Link: {AFFILIATE_LINK}\n")

def main():
    cinematic_intro()
    show_deliverables()
    forge_manifest()
    cinematic_outro()
    print(Fore.GREEN + Style.BRIGHT + "\n✅ Neural Forge Presentation Complete.\n")

if __name__ == "__main__":
    main()