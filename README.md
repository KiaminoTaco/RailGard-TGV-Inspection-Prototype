# RailGard
### TGV Undercarriage Inspection — Multidisciplinary Engineering Prototype

<p align="center">
  <img src="media/images/railgard-prototype-main.png"
       alt="RailGard physical prototype"
       width="900">
</p>

<p align="center">
  <strong>SafeTrack — Robot Autonome d’Inspection Sous-Caisse TGV</strong>
</p>

<p align="center">
  Mechanical Engineering · Robotics · Embedded Systems · Electronics · Inspection
</p>

---

## 1. Project Overview

**RailGard** is a multidisciplinary engineering prototype developed around the concept of a robotic platform for **TGV undercarriage inspection**.

The project brings together mechanical design, robotic actuation, embedded electronics, sensing, communication, data acquisition and inspection-oriented software within one electromechanical system.

The work covers the development of the mobile structure, mechanical integration, a multi-axis robotic subsystem, embedded control platforms, motors and drivers, sensing technologies, communication interfaces and software experiments for image acquisition and inspection.

RailGard was developed in the context of **SafeTrack — Robot Autonome d’Inspection Sous-Caisse TGV**, with the broader objective of studying how robotic and embedded technologies can support railway inspection activities in difficult-to-access areas.

> **Project status:** RailGard is an **engineering prototype / experimental platform**. It is not presented as a certified railway inspection system, an approved railway product, or a replacement for certified railway inspection procedures.

---

## 2. Prototype Demonstration

The most important part of this repository is the **physical prototype**. The images and demonstration video below are intended to document the actual robot, its mechanical structure and its developed subsystems.

### Prototype

<p align="center">
  <img src="media/images/railgard-prototype-front.png"
       alt="RailGard prototype — front view"
       width="420">

  <img src="media/images/railgard-prototype-side.png"
       alt="RailGard prototype — side view"
       width="420">
</p>

<p align="center">
  <img src="media/images/railgard-prototype-robotic-arm.png"
       alt="RailGard prototype — robotic arm"
       width="420">

  <img src="media/images/railgard-prototype-electronics.png"
       alt="RailGard prototype — electronics"
       width="420">
</p>

> Replace the example image filenames above with the actual photographs of the prototype stored in `media/images/`.

### Video Demonstration

The prototype demonstration video is stored directly in the repository:

```text
media/
└── videos/
    └── railgard-prototype-demo.mp4
```

For the README, the following HTML5 video block is included:

<video controls width="900" preload="metadata">
  <source src="media/videos/railgard-prototype-demo.mp4" type="video/mp4">
  Your browser does not support embedded video. [Open the MP4 demonstration](media/videos/railgard-prototype-demo.mp4).
</video>

**[▶ Open the prototype demonstration video](media/videos/railgard-prototype-demo.mp4)**

> **GitHub note:** GitHub's handling of repository-hosted MP4 files can vary between the README renderer, browser and mobile application. If the inline player is not rendered, the link above still provides direct access to the MP4. GitHub officially supports MP4 media uploads, with file-size limits depending on the account type. H.264 is recommended for broad browser compatibility. citeturn0search5

---

## 3. Project Objectives

The project was developed around the following engineering objectives:

- Design a robotic platform adapted to the constraints of TGV undercarriage inspection.
- Develop a mechanically stable mobile structure.
- Study and integrate a multi-axis robotic arm.
- Integrate embedded computing and control platforms.
- Acquire information from cameras and distance/environmental sensors.
- Develop communication between embedded subsystems.
- Explore inspection-oriented image acquisition and processing.
- Integrate motors, drivers, power supply and control electronics.
- Establish a technical basis for further testing, validation and development.

The project is therefore approached as a **system-integration problem**, where mechanical, electrical, embedded and software subsystems must operate as a coherent platform.

---

## 4. Engineering Scope

RailGard combines several engineering disciplines:

| Engineering domain | Main contribution |
|---|---|
| **Mechanical Engineering** | Chassis, CAD, assemblies, dimensioning, stability and structural studies |
| **Robotics** | Multi-axis robotic arm, kinematics, torque studies and actuator integration |
| **Embedded Systems** | Raspberry Pi 5, Jetson Nano, ESP32, Arduino Mega and Teensy-based concepts |
| **Electronics** | Sensors, motor drivers, wiring, power and communication interfaces |
| **Software** | Python, C++, MATLAB/Simulink and inspection-oriented processing |
| **Communication** | Wi-Fi, LoRa, UART, I2C, SPI and GPIO |
| **System Integration** | Integration of mechanical, electrical, embedded and robotic subsystems |

---

## 5. Mechanical Design

Mechanical engineering is a central part of RailGard.

The development work includes:

- mobile chassis architecture;
- aluminium structural design;
- 3D CAD modelling;
- mechanical assemblies;
- engineering drawings;
- mechanical dimensioning;
- Resistance of Materials (RDM) studies;
- stability considerations;
- mass estimation;
- centre-of-gravity considerations;
- integration of motors and actuators.

### Mechanical Documentation

The mechanical documentation is organized as:

```text
mechanical/
├── cad/
├── drawings/
└── calculations/
```

A more detailed drawing structure can be used as the project grows:

```text
mechanical/
└── drawings/
    ├── assembly/
    ├── parts/
    ├── dimensions/
    ├── exploded_views/
    ├── pdf/
    └── images/
```

The repository can therefore contain both the original engineering drawings and the supporting calculations used during development.

---

## 6. Robotic Subsystem

A **multi-axis robotic arm** forms part of the prototype concept.

The engineering study covers:

- multi-axis mechanical configuration;
- kinematic analysis;
- actuator selection and integration;
- torque calculations;
- mechanical interfaces;
- robotic control concepts;
- integration with the mobile platform.

The robotic subsystem is intended to extend the inspection capability of the platform by providing controlled access to areas that may not be reachable by the mobile base alone.

---

## 7. Embedded Electronics

The project includes several embedded computing and control platforms.

### Raspberry Pi 5

The Raspberry Pi 5 is associated with higher-level functions such as:

- communication coordination;
- sensor-data processing;
- camera/image processing;
- higher-level control and decision logic;
- communication with embedded controllers;
- local data handling.

### Other Embedded Controllers

The technical work also discusses or uses:

- **ESP32**
- **Arduino Mega**
- **Teensy**
- **Jetson Nano**

These platforms correspond to different stages or subsystem-level approaches documented during the project.

Because the prototype evolved through several engineering stages, the repository deliberately distinguishes between:

- architecture studied in the technical work;
- experimental implementations;
- functions actually implemented in committed hardware and source code.

---

## 8. Sensors and Inspection

The documented prototype architecture includes several sensing technologies:

- **Raspberry Pi Camera Module 3**
- **RPLIDAR A3M1**
- **SRF10 ultrasonic sensor**
- **LM35 temperature sensor**
- **Sharp GP2Y0A02YK0F infrared distance sensor**
- **IMU**
- **LoRa communication modules**

These elements support:

- image acquisition;
- distance measurement;
- environmental sensing;
- localization/perception concepts;
- communication;
- inspection-oriented data acquisition.

### Wiring Documentation

Electrical and sensor wiring diagrams are organized under:

```text
electronics/wiring/
```

Examples include:

```text
electronics/wiring/diagrams/
├── WIR-001_RaspberryPi_UltrasonicSensor.png
├── WIR-002_RaspberryPi_LM35_TemperatureSensor.png
└── WIR-003_Teensy4.1_RFM9xW_LoRa_Transceiver.png
```

---

## 9. Actuation

The documented actuation system includes:

- stepper motors;
- DC motors;
- servomotors;
- geared motors;
- A4988 stepper drivers;
- L298N motor drivers.

The general actuation chain is:

```text
Embedded Controller
        │
        ▼
   Motor Driver
        │
        ▼
 Motor / Actuator
        │
        ▼
Mechanical Subsystem
```

The exact motor and driver allocation should always be verified against the corresponding electrical drawings and committed source code.

---

## 10. Communication

The project documentation discusses several communication and interface technologies:

- Wi-Fi;
- LoRa;
- UART;
- I2C;
- SPI;
- GPIO;
- MQTT/WebSocket concepts;
- Bluetooth concepts.

These interfaces are associated with communication between controllers, sensors, actuators and external systems.

The repository distinguishes between technologies that were **studied**, technologies used experimentally, and protocols that are actually implemented in the committed prototype.

---

## 11. Software and Inspection Processing

The project includes software experiments related to image acquisition, processing, communication and inspection.

Documented software areas include:

- Raspberry Pi camera image acquisition;
- image comparison;
- OpenCV-based image-difference detection;
- thresholding and contour analysis;
- LoRa image transmission;
- Haar-cascade based object detection;
- TensorFlow-based anomaly-detection workflows.

### Reported Code

Code represented directly in the technical documentation is preserved under:

```text
report-code/
```

with examples such as:

```text
report-code/
├── capture_image_report.py
├── image_difference_report.py
├── lora_transmit_report.py
├── object_detection_report.py
└── cloud_anomaly_detection_report.py
```

### Development Source

Organized development implementations are maintained under:

```text
src/
├── ai/
├── communication/
└── vision/
```

This separation makes it possible to preserve the documented engineering work while keeping the development source structured for future iterations.

---

## 12. System Integration

RailGard follows an interdisciplinary development workflow:

```text
Engineering Requirements
          │
          ▼
    System Design
          │
          ├──────────────► Mechanical Design
          │
          ├──────────────► Electronics
          │
          ├──────────────► Embedded Systems
          │
          └──────────────► Robotics & Control
                                 │
                                 ▼
                         Subsystem Integration
                                 │
                                 ▼
                           Physical Prototype
                                 │
                                 ▼
                        Testing & Demonstration
                                 │
                                 ▼
                          Further Development
```

The objective is not simply to develop isolated components, but to investigate how the different engineering disciplines can be integrated into one functional prototype.

---

## 13. Repository Structure

```text
RailGard/
│
├── README.md
│
├── docs/
│   └── architecture/
│       ├── system-architecture.md
│       └── Architecture_Globale_du_Systeme_de_Commande.png
│
├── mechanical/
│   ├── cad/
│   ├── drawings/
│   └── calculations/
│
├── electronics/
│   ├── schematics/
│   ├── wiring/
│   ├── pcb/
│   └── power/
│
├── robotics/
│
├── embedded/
│
├── report-code/
│
├── src/
│   ├── ai/
│   ├── communication/
│   └── vision/
│
├── requirements/
│
├── simulation/
│
├── media/
│   ├── images/
│   └── videos/
│       └── railgard-prototype-demo.mp4
│
└── tests/
```

---

## 14. Prototype Documentation

The `media/` directory is dedicated to documenting the physical development of the robot.

Recommended structure:

```text
media/
├── images/
│   ├── railgard-prototype-main.png
│   ├── railgard-prototype-front.png
│   ├── railgard-prototype-side.png
│   ├── railgard-prototype-robotic-arm.png
│   └── railgard-prototype-electronics.png
│
└── videos/
    └── railgard-prototype-demo.mp4
```

The image section can later be expanded with:

- prototype photographs;
- different views of the robot;
- robotic-arm photographs;
- electronics photographs;
- assembly stages;
- testing photographs;
- CAD renders;
- experimental results.

This keeps the README visually focused on the **physical prototype**, while detailed technical drawings remain in their dedicated engineering directories.

---

## 15. Project Status

RailGard is documented as an **engineering prototype**.

| Area | Status |
|---|---|
| Mechanical architecture | Engineering development |
| Chassis design | Developed / documented |
| Robotic arm | Studied / integrated |
| Embedded architecture | Developed across multiple subsystems |
| Sensors | Integrated / studied according to subsystem |
| Motors and drivers | Engineering development |
| Communication | Engineering development |
| Inspection software | Experimental / development |
| Physical prototype | Prototype |
| Industrial deployment | Not claimed |
| Railway certification | Not claimed |

These descriptions are intentionally conservative. A concept, experiment or documented architecture should not be interpreted as a fully validated industrial capability unless the repository provides corresponding implementation and validation evidence.

---

## 16. Scope and Limitations

RailGard is an **experimental engineering prototype**.

The project does not claim that the current prototype:

- is deployed on operational TGV trains;
- is certified for railway operation;
- is approved for industrial deployment;
- replaces certified railway inspection procedures;
- has completed every validation required for real-world railway operation;
- constitutes a complete autonomous railway inspection solution.

Some technologies and architectures documented in the project represent engineering studies, experimental implementations or possible future development.

This distinction is important when interpreting the hardware, software, communication protocols and autonomous functions documented in this repository.

---

## 17. Future Development

Potential future development includes:

- further mechanical optimisation;
- refinement of the robotic arm;
- improved actuator control;
- expanded sensor integration;
- improved communication between subsystems;
- more extensive image-processing validation;
- additional anomaly-detection experiments;
- improved autonomous behaviour;
- additional testing scenarios;
- improved inspection data acquisition;
- further study of railway and industrial feasibility.

These items are **development directions**, not claims about capabilities already validated by the current prototype.

---

## 18. Project Recognition

The SafeTrack project was developed in the **SIANA / InnovAM'26** context and is documented as having received:

**2nd Place — Prix Innovation Arts et Métiers**

The project brings together work in:

- mechanical engineering;
- robotics;
- embedded systems;
- electronics;
- automation;
- electromechanical integration;
- railway-oriented engineering.

---

## 19. Project Team

- **Aymane El Haoudar**
- **Mohamed Amine Mohib**
- **Yassine Benkhlouk**
- **Nassim Bouziki**

---

## 20. Technical Stack

### Mechanical Engineering

`CATIA V5` · `SolidWorks` · `OpenSCAD` · `PyCATIA` · `RDM`

### Embedded Systems

`Raspberry Pi 5` · `Jetson Nano` · `ESP32` · `Arduino Mega` · `Teensy`

### Programming

`Python` · `C++` · `MATLAB` · `Simulink`

### Robotics

`ROS 2` · `Stepper Motors` · `Servomotors` · `Kinematics` · `Control`

### Electronics and Simulation

`Proteus` · `Altium Designer` · `Motor Drivers` · `Sensors` · `LoRa`

---

## 21. Academic and Engineering Perspective

RailGard documents the development of a multidisciplinary robotic prototype rather than a collection of independent files.

The repository connects:

```text
Mechanical Design
       │
       ▼
Electronics & Power
       │
       ▼
Embedded Computing
       │
       ▼
Sensing & Communication
       │
       ▼
Software & Data Processing
       │
       ▼
Robotics & Control
       │
       ▼
Physical Prototype
       │
       ▼
Testing & Demonstration
```

The objective of this repository is to make the engineering process traceable and understandable for engineers, researchers, students and future contributors who may want to study, reproduce or extend the work.

---

## 22. Documentation

Additional technical documentation is available in:

```text
docs/
```

including the system architecture documentation:

[System Architecture](docs/architecture/system-architecture.md)

Mechanical, electrical, wiring and source-code documentation should be consulted together when analysing a particular subsystem.

---

<p align="center">
  <strong>RailGard</strong><br>
  TGV Undercarriage Inspection — Engineering Prototype
</p>

<p align="center">
  <em>Design · Integration · Experimentation · Testing</em>
</p>
