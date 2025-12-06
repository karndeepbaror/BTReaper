****🛰️ BlueSpy — Bluetooth Audio Capture & Hacking****

> Record & replay audio from Bluetooth devices without user awareness — for research & educational purposes only.


<p align="center">
  <img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python_3.11+-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Developer-Karndeep_Baror-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Bluetooth-BlueZ_Stack-0A84FF?style=for-the-badge">
</p>

***⚠️ Disclaimer:***

This project is for security research, demo, awareness & educational purposes ONLY.
Unauthorized Bluetooth interception may be illegal in your country.
The author is not responsible for misuse.


***📌 Overview:***

`BlueSpy` is a Proof of Concept (PoC) tool demonstrating how audio can be:

> Automatically paired
> Connected
> Recorded
> Replayed

from a vulnerable Bluetooth audio device without user notice.

***🎟️Presented At:***

BSAM: Seguridad en Bluetooth — RootedCON Madrid 2024
Expanded & improved by: Karndeep Baror (Cryptonic Area)

This PoC highlights weaknesses in BlueZ-based Bluetooth pairing and audio handling, especially in consumer earbuds/headsets.


**🔧 Features***

Feature	Description

🔍 Automatic Device Discovery	Scans & identifies nearby BT audio devices.
🔐 Silent Pairing Attempt	Attempts pairing without user attention
🎧 Covert Connection	Invisible connect attempt
🎙 Audio Recording	Captures microphone stream
🔊 Replay Audio	Plays back captured audio
🛠 Modular Components	Pair / connect / record / playback individually runnable

***🏗 Project Structure:***
```
BlueSpy/
│
├── BlueSpy.py         → Main automation script
├── core.py            → Pair, connect, record & playback logic
├── interface.py       → UI helpers & color output
├── pair.py            → Standalone pairing module
├── connect.py         → Standalone connection module
├── just_record.py     → Standalone recording module
└── README.md          → Documentation (this file)
```

***📦 Requirements:***

> `BlueSpy` relies on Linux Bluetooth & audio tools.

***BlueZ Tools 🔥***

Tool	Package

bluetoothctl	bluez-utils
btmgmt	bluez-utils


***PulseAudio / PipeWire 👀:***

Tool	Package

pactl	libpulse
parecord	libpulse
paplay	libpulse


***Minimum 🖥️:***

Python 3.11+
Working BlueZ stack
PulseAudio or PipeWire audio server


***📡 Setup:***

**1️⃣ Prepare the Bluetooth earbuds/headset**

*Ensure:*

Discoverable mode
Connectable mode
Microphone enabled (varies by model)


**2️⃣ Ensure device is NOT already connected**

Some earbuds support only one active connection.


***🚀 Execution:***

**Step 1 — Discover target MAC**
```
bluetoothctl
[bluetooth]# scan on
```
Copy the Bluetooth address.

**Step 2 — Run BlueSpy**
``
sudo python BlueSpy.py -a <MAC_ADDRESS>
```
**Example:**
`sudo python BlueSpy.py -a DC:23:A4:11:9B:5C`

***💻 BlueSpy will:***

1. Attempt pairing.
2. Connect.
3. Record audio.
4. Optionally replay audio.


🧪 Troubleshooting

**Pairing Issues (btmgmt):**
```
sudo btmgmt power on
sudo btmgmt pairable on
sudo btmgmt connectable on
```

**Connection Issues (bluetoothctl):**
```
bluetoothctl
[bluetooth]# power on
[bluetooth]# scan on
[bluetooth]# connect <MAC>
```


***⭐ Support:***

If this project helped you, please `⭐ Star` the repo on GitHub.
For improvements, PRs are welcome

***👤 Author***

Made with ❤️ by *__Karndeep Baror__*  
**LinkedIn:** [linkedin.com/in/karndeepbaror](https://www.linkedin.com/in/karndeepbaror)
