# ⚙️ RailGard — TGV Undercarriage Inspection

Engineering prototype for robotic inspection of TGV undercarriage systems.

> **Repository note:** The code in this repository is organized from the code listings visible in the RailGard technical report. Some listings are experimental or illustrative and were not presented in the report as a fully validated production software stack.

## Code included

- Raspberry Pi image capture
- OpenCV image-difference detection
- LoRa image transmission
- OpenCV Haar-cascade object detection
- TensorFlow anomaly-detection workflow

## Repository structure

```text
RailGard-TGV-Inspection-Prototype/
├── README.md
├── requirements/
│   ├── requirements-vision.txt
│   └── requirements-ai.txt
├── src/
│   ├── vision/
│   │   ├── capture_image.py
│   │   ├── image_difference.py
│   │   └── object_detection.py
│   ├── communication/
│   │   └── lora_transmit.py
│   └── ai/
│       └── cloud_anomaly_detection.py
├── report-code/
│   ├── capture_image_report.py
│   ├── image_difference_report.py
│   ├── lora_transmit_report.py
│   ├── object_detection_report.py
│   └── cloud_anomaly_detection_report.py
├── docs/
├── mechanical/
├── electronics/
├── embedded/
├── robotics/
├── software/
├── simulation/
├── media/
└── tests/
```

## Important distinction

`report-code/` contains transcriptions of the code listings shown in the technical report.

`src/` contains cleaned/corrected implementations that preserve the intended function of those report listings. They should still be tested against the actual hardware, operating system, LoRa driver, camera stack and trained model before being presented as validated robot software.

## Project scope

The report describes a Raspberry Pi 5 master unit, ESP32 subsystem control, camera-based inspection, LiDAR navigation, LoRa communication, OpenCV-based perception and cloud/ML anomaly processing.

RailGard is an engineering/experimental prototype and is not presented as a certified railway inspection system.
