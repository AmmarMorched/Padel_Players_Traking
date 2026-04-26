# 🎾 Padel Player & Ball Tracking — Computer Vision Module

Real-time detection and tracking of padel players and ball using YOLOv5, with live minimap visualization of court positions.

> **Note:** This repository contains the computer vision module only. The full system — including piezoelectric floor sensor integration, multi-source data fusion, and Raspberry Pi deployment — was developed for a client and is protected under NDA.

---

## 📌 What It Does

This module processes a live or recorded court video feed and produces two outputs simultaneously:

- **Annotated video stream** — bounding boxes around detected players and ball in real time
- **Live minimap** — a top-down 2D court representation showing player and ball positions updated every frame

The minimap gives coaches and analysts an instant spatial view of court coverage, player movement patterns, and ball trajectory — without needing to watch raw footage.

---

## 🎬 Demo

```
[Camera Feed]
      ↓
  YOLOv5s Detection
  (players + ball)
      ↓
  Homography Transform
  (court → minimap coordinates)
      ↓
  [Annotated Feed]  +  [Live Minimap]
```

> Demo video inside the video folder

---

## 🧠 How It Works

### 1. Detection — YOLOv5s
- YOLOv5s model detects players and ball each frame
- Chosen for its balance of speed and accuracy on edge hardware
- Custom-trained or fine-tuned weights on padel court footage

### 2. Court Homography
- Four court corner reference points define the perspective transform
- Each detected bounding box centroid is mapped from camera coordinates to minimap coordinates using OpenCV's `getPerspectiveTransform`

### 3. Minimap Rendering
- A scaled top-down court template is drawn each frame
- Player positions rendered as colored circles
- Ball position rendered as a distinct marker
- Updated in real time alongside the main video feed

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Object Detection | YOLOv5s |
| Computer Vision | OpenCV |
| Deep Learning | PyTorch |
| Language | Python 3.10+ |
| Visualization | OpenCV drawing API |

---

## 📁 Project Structure

```
Padel_Players_Tracking/
│
├── main.py                  # Entry point — runs detection + minimap
├── tracker.py               # Player and ball tracking logic
├── minimap.py               # Homography + minimap rendering
├── requirements.txt         # Dependencies
├── weights/
│   └── best.pt              # YOLOv5 trained weights
├── court_template/
│   └── court.png            # Top-down court reference image
└── utils/
    └── helpers.py           # Coordinate transform utilities
```

> Adapt structure above to match your actual repo layout

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/AmmarMorched/Padel_Players_Traking.git
cd Padel_Players_Traking

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download YOLOv5
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt
```

---

## 🚀 Usage

```bash
# Run on a video file
python main.py --source video.mp4

# Run on webcam
python main.py --source 0

# Run with custom weights
python main.py --source video.mp4 --weights weights/best.pt
```

---

## 📐 Court Reference Points Setup

To calibrate the homography for your specific camera angle, define the 4 court corners in `main.py`:

```python
# Pixel coordinates of court corners in your camera feed
COURT_CORNERS_SRC = [
    [x1, y1],  # Top-left
    [x2, y2],  # Top-right
    [x3, y3],  # Bottom-right
    [x4, y4],  # Bottom-left
]
```

---

## 🔗 Full System Context

This module is part of a larger proprietary sports analytics system that includes:

- **Piezoelectric floor sensors** (ESP32) — detect ball impact force and position
- **Multi-source data fusion** — synchronizes vision tracking with sensor events on Raspberry Pi
- **Real-time analytics pipeline** — unified court event stream for performance analysis

The full system was delivered to a client under NDA. This repository demonstrates the computer vision layer independently.

---

## 👤 Author

**Morched Ammar** — Embedded Systems & AI Engineer

- 🔗 [LinkedIn](www.linkedin.com/in/morched-ammar-805407197)
- 📧 morched99@yahoo.com
