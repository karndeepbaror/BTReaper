***🛰️ BlueSpy — Bluetooth Audio Capture & Hacking***

> Record & replay audio from Bluetooth devices without user awareness — for research & educational purposes only.

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python_3.11+-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Developer-Karndeep_Baror-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Bluetooth-BlueZ_Stack-0A84FF?style=for-the-badge">
</p>
---

****⚠️ Disclaimer****

This project is for security research, demo, awareness & educational purposes ONLY.
Unauthorized Bluetooth interception may be illegal in your country.
The author is not responsible for misuse.




***📌 Overview***

`BlueSpy` is a Proof of Concept (PoC) tool demonstrating how audio can be:

✔ Automatically paired.
✔ Connected.
✔ Recorded.
✔ Replayed.

from a vulnerable Bluetooth audio device without the user noticing.

****This PoC was presented at:***"

> 🎤 BSAM: Seguridad en Bluetooth
🏁 CryptonicArea 2025 - `Karndeep Baror`



The project explores weaknesses in Bluetooth pairing & audio protocols, especially in consumer earbuds/headsets.


****🔧 Features****

Feature	Description

🔍 Automatic Device Discovery	Scans & identifies nearby BT audio devices.
🔐 Silent Pairing Attempt	Uses BlueZ vulnerabilities to pair.
🎧 Covert Connection	Connects even when the device isn’t expecting.
🎙 Record Audio	Captures microphone stream.
🔊 Replay Audio	Plays back captured stream.
🛠 Standalone Modules	Pair / connect / record / playback scripts.


****🏗 Project Structure****
```
BlueSpy/
│
├── BlueSpy.py         → Main automation script
├── core.py            → Pair, connect, record & playback logic
├── interface.py       → Colors, UI, log helpers
├── pair.py            → Standalone pairing test
├── connect.py         → Standalone connection test
├── just_record.py     → Standalone recording test
└── README.md          → Documentation (this file)
```

****📦 Requirements****

This PoC depends on standard Linux Bluetooth & audio tools.

****🔵 BlueZ Tools***oool
olllol	Package

bluetoothctl	bluez-utils
btmgmt	bluez-utils


****🔊 PulseAudio / PipeWire Tools****

Tool	Package

pactl	libpulse
parecord	libpulse
paplay	libpulse


****Minimum:****

Python 3.11+

Working BlueZ installation

PulseAudio or PipeWire



****📡 Setup Instructions****

**1️⃣ Put earbuds/headset in:**

✔ Discoverable mode
✔ Connectable mode
✔ Microphone-enabled mode (varies by model)

**2️⃣ Ensure the device is not already connected**

Some earbuds only allow a single active connection.


****🚀 Execution****

**🔍 Step 1 — Discover target Bluetooth address**
```
$ bluetoothctl
[bluetooth]# scan on
```

Locate the MAC address of your earbuds.


****🎯 Step 2 — Run BlueSpy****
```
$ sudo python BlueSpy.py -a <MAC_ADDRESS>
```

Example:
```
$ sudo python BlueSpy.py -a DC:23:A4:11:9B:5C
```

***BlueSpy will automatically:***

1️⃣ Attempt pairing
2️⃣ Attempt connection
3️⃣ Record audio
4️⃣ Optionally replay audio

****🧪 Troubleshooting****

Pairing Issues (btmgmt)

Run manually:
```
$ sudo btmgmt power on
$ sudo btmgmt pairable on
$ sudo btmgmt connectable on
```

Connect Issues (bluetoothctl)
```
$ bluetoothctl
[bluetooth]# power on
[bluetooth]# scan on
[bluetooth]# connect <MAC>
```

****Audio Recording Issues:****

**Check available sources:**
```
$ pactl list sources
```

**Then test recording:**
```
$ parecord test.wav
```

