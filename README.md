****🛰️ BlueSpy — Bluetooth Audio Capture & Hacking Script****

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python_3.11+-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Developer-Karndeep_Baror-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Bluetooth-BlueZ_Stack-0A84FF?style=for-the-badge">
</p>

> Proof-of-concept tool to demonstrate covert audio capture from Bluetooth devices — research & educational purposes only.

***⚠️ Legal Warning***

• This project is for research & educational purposes only.
• Unauthorized use of BlueSpy to intercept audio is illegal.
• The author is not responsible for misuse.

***🎯 Overview***

`BlueSpy` demonstrates a full exploit chain on vulnerable Bluetooth audio devices:

1. 🔍 Automatic device discovery
2. 🔐 Silent pairing attempt
3. 📡 Hidden connection establishment
4. 🎙️ Microphone stream recording
5. 🔊 Audio replay

It is intended to showcase weaknesses in consumer Bluetooth audio protocols and raise security awareness.

***🔧 Features***

• **Automatic device scan:**  Detects nearby audio devices.

• **Silent pairing:**  Attempts pairing without user prompt.

• **Covert connection:** Connects even if device is idle.

• **Audio capture:** Records microphone stream using PulseAudio/PipeWire.

• **Audio playback:**  Replays the captured audio.

• **Modular tools:** Separate scripts for pair/connect/record.

***🏗 Project Structure:***

```
BlueSpy/
├── BlueSpy.py          → Main automation script
├── core.py             → Logic for pairing, connecting, recording, playback
├── interface.py        → Logging, colors, UI helpers
├── pair.py             → Manual pairing test
├── connect.py          → Manual connection test
├── just_record.py      → Manual recording test
└── README.md           → This documentation
```

***📦 Requirements:***
*Linux Tools:*

 `bluetoothctl` and `btmgmt` (from `bluez-utils` )

 `pactl` `parecord`  `paplay` (from `libpulse` )


***🔩 Software Requirements:***

 Python 3.11+

 Working `BlueZ stack`

 `PulseAudio` or `PipeWire`

**📷 Screenshot:**
![BlueSpy](https://github.com/user-attachments/assets/5697bcd0-9685-4e3b-9150-80a209ca294b)

***📡 Device Setup***
```
git clone https://github.com/karndeepbaror/BlueSpy
cd Blue Spy 
./BlueSpy
python BlueSpy.py
```

*1. Put earbuds/headset in:*

    • Discoverable mode

    • Connectable mode

    • Microphone-enabled mode


*2. Ensure the device is `not connected` to another device.*

*3. Some earbuds only activate microphone `when worn.`*


***🚀 Usage***

*1️⃣ Discover the Bluetooth device*

```
$ bluetoothctl
[bluetooth]# scan on
```

*2️⃣ Run BlueSpy*

```
$ sudo python BlueSpy.py -a <MAC_ADDRESS>
```

Example:

```
$ sudo python BlueSpy.py -a DC:23:A4:11:9B:5C
```

**BlueSpy will automatically:**

• Attempt pairing 🔐
• Establish connection 📡
• Start recording 🎙️
• Ask to replay audio 🔊


***🧪 Troubleshooting:***

Pairing issues:

```
$ sudo btmgmt power on
$ sudo btmgmt pairable on
$ sudo btmgmt connectable on
```

**Connection issues:**

```
$ bluetoothctl
[bluetooth]# power on
[bluetooth]# scan on
[bluetooth]# connect <MAC>
```

**Audio recording issues:**
*Check sources:*

```
$ pactl list sources
```

*Test recording:*

```
$ parecord test.wav
```

***🔐 Security Notes:***

*BlueSpy highlights common vulnerabilities:*

• Weak `Bluetooth pairing` procedures

• Microphone `auto‑activation`

• Hidden `connection flaws`

• Lack of `mutual authentication`



****🖥️ Developer Information****

**👤 Developer:** __Karndeep Baror__

_🔗 LinkedIn:_  [ Connect Here ](https://www.linkedin.com/in/karndeepbaror)

_💬 WhatsApp Community:_  [ Join Now ](https://whatsapp.com/channel/0029Vb6plDSBKfi3qGz2fq0f)

> If this project helped you, please `⭐ star` the repo on GitHub.
