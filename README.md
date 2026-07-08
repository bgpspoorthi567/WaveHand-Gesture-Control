# ✋ WaveHand - Hand Gesture Controlled Light using OpenCV & Arduino

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Arduino](https://img.shields.io/badge/Arduino-UNO-teal)

A computer vision project that allows users to control an LED using simple hand gestures. The system uses **MediaPipe** to detect hand landmarks, **OpenCV** for real-time video processing, and **Arduino** to control the hardware through serial communication.

---

## 📌 Project Overview

This project demonstrates real-time hand gesture recognition for hardware control.

After detecting a hand, the system waits for a stable position and recognizes the following gestures:

| Gesture | Action |
|----------|--------|
| 👍 Thumbs Up (Closed Fist) | Turn LED ON |
| 👎 Thumbs Down (Closed Fist) | Turn LED OFF |

The recognized gesture is sent to the Arduino through serial communication, which switches the LED accordingly.

---

## 🎯 Features

- ✅ Real-time hand tracking
- ✅ Gesture recognition using MediaPipe
- ✅ Arduino serial communication
- ✅ LED ON/OFF control
- ✅ Stable gesture detection
- ✅ Easy to modify for other automation projects

---

## 🛠 Hardware Required

- Arduino UNO
- LED
- 220Ω Resistor
- Breadboard
- Jumper Wires
- USB Cable
- Webcam

---

## 💻 Software Required

- Python 3.x
- Arduino IDE
- OpenCV
- MediaPipe
- PySerial

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
WaveHand-Gesture-Control
│
├── Arduino
│   └── WaveHand.ino
│
├── Python
│   └── WaveHand.py
│
├── Demo
│   ├── demo.mp4
│   └── screenshot.png
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ How It Works

1. The webcam captures live video.
2. OpenCV processes each video frame.
3. MediaPipe detects hand landmarks.
4. The program checks whether the gesture is:
   - 👍 Thumbs Up
   - 👎 Thumbs Down
5. Python sends a serial command to the Arduino.
6. Arduino switches the LED ON or OFF.

---

## 🔄 Workflow

```
Webcam
   │
   ▼
OpenCV
   │
   ▼
MediaPipe Hand Detection
   │
   ▼
Gesture Recognition
   │
   ▼
Python
   │
   ▼
Serial Communication
   │
   ▼
Arduino UNO
   │
   ▼
LED ON / OFF
```

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/your-username/WaveHand-Gesture-Control.git
```

Move into the project folder:

```bash
cd WaveHand-Gesture-Control
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Update the Arduino COM port inside `WaveHand.py`:

```python
arduino = serial.Serial("COM3", 9600)
```

Run the Python program:

```bash
python WaveHand.py
```

---

## 📸 Demo

> Add your project screenshots and demo video inside the **Demo** folder.

Example:

```
Demo/
├── demo.mp4
└── screenshot.png
```

---

## 🔮 Future Enhancements

- Multiple gesture recognition
- Home automation
- Fan and appliance control
- Voice + Gesture control
- IoT integration
- Mobile application support

---

## 📚 Technologies Used

- Python
- OpenCV
- MediaPipe
- Arduino
- PySerial

---

## 👨‍💻 Author

**B G P Spoorthi**

If you found this project helpful, consider giving it a ⭐ on GitHub!
