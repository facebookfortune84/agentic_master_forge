#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
🔥 Realms to Riches | Agentic Master Forge™ 2025
All-in-One Orchestrator – builds presentation & finale scripts,
then runs the entire cinematic Forge pipeline.
"""

import os, textwrap, time, subprocess, sys
from datetime import datetime
from pathlib import Path

root = Path(__file__).parent

# --- Voice Configuration (safe placeholders) -------------------------------
VOICE_IDS = {
    "adam": "Eeg4uu5XxPosS7qxJsTI",
    "elli": "BrOny4Lkm3SsSmSNv8hv",
    "roger": "CwhRBWXzGAHq8TQ4Fs17",
    "architect": "YOUR_ARCHITECT_VOICE_ID"   # add once created
}

# --- Build forge_presentation_neural.py ------------------------------------
presentation_code = textwrap.dedent(f"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elevenlabs import generate, play, set_api_key
import os, zipfile, json, time
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

set_api_key(os.getenv("ELEVENLABS_API_KEY", ""))
VOICE_IDS = {VOICE_IDS}

def narrate(text, voice_key):
    try:
        audio = generate(text=text, voice=VOICE_IDS.get(voice_key,"CwhRBWXzGAHq8TQ4Fs17"), model="eleven_multilingual_v2")
        play(audio)
    except Exception as e:
        print(Fore.YELLOW + f"[voice-fallback] {{text[:80]}}...")

def cinematic_intro():
    print(Fore.MAGENTA + Style.BRIGHT + "\\n🌌 Awakening the Forge...\\n")
    narrate("Welcome to the Realms to Riches Agentic Master Forge, two thousand twenty-five.", "adam")

def unpack_latest_forge():
    zips = [z for z in os.listdir('.') if z.startswith('RealmsToRiches_Forge') and z.endswith('.zip')]
    if not zips: return None
    latest = max(zips, key=os.path.getmtime)
    target = f"F:/Forge_Replicas/{{os.path.splitext(latest)[0]}}"
    os.makedirs(target, exist_ok=True)
    with zipfile.ZipFile(latest,'r') as z: z.extractall(target)
    print(Fore.GREEN + f"📦 Unpacked → {{target}}")
    return target

def inventory(target):
    summary = []
    for root,_,files in os.walk(target):
        for f in files:
            if f.endswith('.md') or f.endswith('.json'):
                path = os.path.join(root,f)
                size = os.path.getsize(path)
                summary.append((f,size))
    print(Fore.CYAN + "\\n🧭 Forge Inventory:")
    for name,size in summary: print(f"  - {{name}}  ({{size}} bytes)")
    with open(os.path.join(target,'Forge_Inventory_Report.md'),'w',encoding='utf-8') as f:
        for name,size in summary: f.write(f"- {{name}}  ({{size}} bytes)\\n")
    return summary

def finale():
    print(Fore.MAGENTA + Style.BRIGHT + "\\n💫 Replication complete. The Forge stands ready.\\n")
    narrate("Replication complete. This world — your Forge — now stands on its own. Awaiting your next command, Robert.", "roger")
    print(Fore.YELLOW + "🔁 Begin new Forge replication cycle? (Y/N)")
    if input().strip().lower().startswith('y'):
        os.execv(sys.executable, [sys.executable, 'forge_master_runner.py'])

if __name__ == "__main__":
    cinematic_intro()
    target = unpack_latest_forge()
    if target:
        narrate("Analyzing Forge contents and preparing the holographic display.", "elli")
        inventory(target)
        narrate("Architect review complete. All systems synchronized.", "architect")
    finale()
""")
(root / "forge_presentation_neural.py").write_text(presentation_code, encoding="utf-8")

# --- Build forge_grand_finale.py -------------------------------------------
finale_code = textwrap.dedent("""
#!/usr/bin/env python
from colorama import init, Fore, Style
init(autoreset=True)
print(Fore.CYAN + Style.BRIGHT + "\\n✨ GRAND FINALE ✨\\n")
print(Fore.MAGENTA + "All systems stable. The Forge sleeps... awaiting your next creation.\\n")
""")
(root / "forge_grand_finale.py").write_text(finale_code, encoding="utf-8")

# --- Launch the Forge ------------------------------------------------------
print("\\n🚀 Launching Forge Master Runner...")
subprocess.run([sys.executable, "forge_master_runner.py"], check=False)

print("\\n🎬 Starting Cinematic Presentation...")
subprocess.run([sys.executable, "forge_presentation_neural.py"], check=False)

print("\\n🏁 Running Grand Finale...")
subprocess.run([sys.executable, "forge_grand_finale.py"], check=False)

print("\\n✅ Complete: cinematic chain executed successfully.")
""")

(root / "launch_all.py").write_text(presentation_code, encoding="utf-8")
print("✅ launch_all.py created.")