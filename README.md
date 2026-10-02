<div align="center">

# ⚙️ RAILGARD

### TGV Undercarriage Inspection — Engineering Prototype

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=0F172A&center=true&vCenter=true&width=850&lines=Mechanical+Engineering+%E2%80%A2+Embedded+Systems+%E2%80%A2+Robotics;Designing+%E2%80%A2+Integrating+%E2%80%A2+Validating;Engineering+Prototype+for+Railway+Inspection" alt="Typing SVG" />

<br>

![Engineering Prototype](https://img.shields.io/badge/STATUS-ENGINEERING%20PROTOTYPE-0f172a?style=for-the-badge)
![Robotics](https://img.shields.io/badge/ROBOTICS-ROS%202-334155?style=for-the-badge)
![Railway](https://img.shields.io/badge/DOMAIN-RAILWAY%20INSPECTION-475569?style=for-the-badge)
![InnovAM](https://img.shields.io/badge/INNOVAM%2726-2nd%20PLACE-b45309?style=for-the-badge)

</div>

---

## 🚄 Project Overview

**RailGard** is an **engineering and experimental prototype** developed around the concept of a robotic platform for **TGV undercarriage inspection**.

The project brings together:

- ⚙️ Mechanical design and dimensioning
- 🤖 Multi-axis robotics
- 🔌 Embedded electronics
- 🧠 Computing and control
- 🔋 Motor, driver and battery integration
- 📡 Communication between subsystems
- 📊 Instrumentation and data acquisition

> **Important:** RailGard is presented as an **engineering prototype / experimental platform**. It is **not a deployed railway inspection robot**, and this repository does not claim operational use, railway certification, or deployment on real TGV trains.

---

## 🎯 Engineering Objective

The project explores how mechanical, electrical and software engineering can be integrated into a robotic architecture intended to support future railway inspection applications.

### Core engineering objectives

```text
Mechanical Structure
        │
        ▼
Robotic Manipulation
        │
        ▼
Embedded Electronics
        │
        ▼
Motor / Actuator Control
        │
        ▼
Communication & Data Acquisition
        │
        ▼
Integrated Engineering Prototype
```

The work focuses on **engineering integration**, rather than presenting a finished industrial product.

---

## 🧩 System Architecture

```text
                         ┌───────────────────────┐
                         │      RAILGARD         │
                         │ Engineering Prototype │
                         └───────────┬───────────┘
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          │                          │                          │
          ▼                          ▼                          ▼
 ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
 │ Mechanical      │       │ Embedded        │       │ Robotics &      │
 │ Architecture    │       │ Electronics     │       │ Control         │
 └────────┬────────┘       └────────┬────────┘       └────────┬────────┘
          │                         │                         │
          ▼                         ▼                         ▼
      Chassis                  Raspberry Pi 5              ROS 2
      CATIA V5                 Jetson Nano                  Motors
      RDM                      ESP32                        Actuators
      Stability               Arduino Mega                 Integration
      Mass / CG               Drivers
                               Power
                                     │
                                     └──────────┬───────────┘
                                                ▼
                                  ┌─────────────────────────┐
                                  │ Communication between   │
                                  │ integrated subsystems   │
                                  └─────────────────────────┘
```

---

## ⚙️ Mechanical Engineering

The mechanical work covers the design and dimensioning of the main structural elements.

### Main areas

- **CATIA V5** mechanical design
- Aluminium chassis architecture
- Structural dimensioning
- Resistance of Materials (**RDM**)
- Stability analysis
- Mass estimation
- Centre-of-gravity considerations
- Mechanical assembly
- Integration of actuated subsystems

### Engineering workflow

```text
Requirements
     ↓
Mechanical Architecture
     ↓
3D CAD Design
     ↓
Dimensioning / RDM
     ↓
Mass & Stability
     ↓
Integration
```

---

## 🤖 Multi-Axis Robotic Arm

A multi-axis robotic arm was studied as part of the prototype architecture.

### Engineering work

- Multi-axis mechanical design
- Kinematic study
- Torque calculations
- Actuator integration
- Mechanical/robotic interface definition
- Integration with the overall prototype architecture

```text
Mechanical Design
       ↓
Kinematic Study
       ↓
Torque Analysis
       ↓
Actuator Selection / Integration
       ↓
Robotic Subsystem
```

---

## 🔌 Embedded Electronics

The prototype architecture integrates several embedded platforms for subsystem control and communication.

<p align="center">
  <img src="https://skillicons.dev/icons?i=raspberrypi,arduino,cpp,python" />
</p>

### Platforms

| Platform | Engineering role |
|---|---|
| **Raspberry Pi 5** | Embedded computing / system integration |
| **Jetson Nano** | Embedded computing platform |
| **ESP32** | Embedded subsystem control |
| **Arduino Mega** | Control of different subsystems |
| **Drivers** | Motor / actuator interfacing |
| **Battery supply** | Prototype power architecture |

The exact allocation of functions can evolve as the prototype architecture is developed.

---

## ⚙️ Motors, Drivers & Power

The system integrates:

- Electric motors
- Motor drivers
- Actuators
- Battery power
- Embedded controllers
- Interconnection between subsystems

### Integration concept

```text
Battery
  │
  ├──────────────► Embedded Electronics
  │
  └──────────────► Motor Drivers
                         │
                         ▼
                      Motors
                         │
                         ▼
                    Mechanical
                     System
```

---

## 🧠 Robotics & Control

The project uses robotics and control concepts to connect the mechanical and embedded layers.

### Technologies

<p align="center">
  <img src="https://skillicons.dev/icons?i=ros,python,cpp" />
</p>

- **ROS 2**
- Python
- C++
- MATLAB / Simulink
- Stepper motors
- Servomotors
- Actuator control
- Electromechanical integration

---

## 📊 Instrumentation & Data Acquisition

The prototype architecture also considers:

- Instrumentation
- Data acquisition
- Communication between subsystems
- Embedded data handling
- Integration of sensing/control elements

The repository should distinguish clearly between **implemented prototype elements** and **future development concepts**.

---

## 🏗️ Engineering Workflow

```text
                 ENGINEERING REQUIREMENTS
                           │
                           ▼
                ┌─────────────────────┐
                │ System Architecture │
                └──────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     Mechanical        Electronics       Robotics
          │                │                │
          ▼                ▼                ▼
       CATIA V5        Embedded HW       ROS 2
       RDM             Controllers       Actuators
       Stability      Drivers           Kinematics
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                  SYSTEM INTEGRATION
                           │
                           ▼
                ENGINEERING PROTOTYPE
```

---

## 🧱 Mechanical + Electronics + Software

RailGard is fundamentally a **cross-disciplinary engineering project**.

| Engineering layer | Main technologies |
|---|---|
| Mechanical Design | CATIA V5, SolidWorks, RDM |
| Robotics | ROS 2, motors, servomotors |
| Embedded | Raspberry Pi 5, Jetson Nano, ESP32, Arduino Mega |
| Programming | Python, C++, MATLAB |
| Simulation | MATLAB / Simulink, Proteus |
| Automation | PyCATIA |
| System Integration | Drivers, power, communication |

---

## 🛠️ Technical Stack

### CAD & Mechanical Engineering

<p align="center">
  <img src="https://skillicons.dev/icons?i=solidworks" />
</p>

`CATIA V5` · `SolidWorks` · `OpenSCAD` · `PyCATIA` · `RDM`

### Embedded & Electronics

<p align="center">
  <img src="https://skillicons.dev/icons?i=raspberrypi,arduino,cpp,python" />
</p>

`Raspberry Pi 5` · `Jetson Nano` · `ESP32` · `Arduino Mega` · `Drivers` · `Power`

### Robotics & Control

`ROS 2` · `Stepper Motors` · `Servomotors` · `Kinematics` · `Control`

### Simulation & Engineering Tools

`MATLAB` · `Simulink` · `Proteus`

---

## 🧪 Prototype Development

The project is structured as an engineering prototype rather than a finished industrial system.

### Development philosophy

```text
Concept
  ↓
Engineering Design
  ↓
Dimensioning
  ↓
Subsystem Integration
  ↓
Prototype Development
  ↓
Validation & Iteration
  ↓
Future Industrial Study
```

Each subsystem can be developed and refined independently before being integrated into the global architecture.

---
 
## 📁 Suggested Repository Structure

```text
RailGard/
│
├── README.md
│
├── mechanical/
│   ├── cad/
│   ├── calculations/
│   └── drawings/
│
├── electronics/
│   ├── schematics/
│   ├── pcb/
│   └── power/
│
├── embedded/
│   ├── arduino/
│   ├── esp32/
│   └── raspberry_pi/
│
├── robotics/
│   ├── ros2/
│   ├── kinematics/
│   └── control/
│
├── software/
│   ├── python/
│   └── cpp/
│
├── documentation/
│   ├── reports/
│   └── technical_notes/
│
├── media/
│   ├── images/
│   └── videos/
│
└── tests/
```

> This structure is a **recommended organization** for the repository. Adapt it to the files actually committed to the project.

---

## 🖼️ Prototype Gallery

Add project visuals here as the repository grows.

```markdown
<p align="center">
  <img src="media/images/railgard-overview.png" width="850">
</p>

<p align="center">
  <img src="media/images/mechanical-design.png" width="420">
  <img src="media/images/electronics.png" width="420">
</p>
```

Recommended visuals:

- Full prototype
- CATIA V5 chassis
- Robotic arm
- Electronics architecture
- Embedded boards
- Motor/driver integration
- Engineering drawings
- System architecture

---

## 👨‍🔧 Engineering Contributions

### Mechanical

- Chassis architecture
- CATIA V5 design
- Mechanical dimensioning
- RDM
- Stability
- Mass and centre-of-gravity considerations

### Robotics

- Multi-axis robotic arm
- Kinematic studies
- Torque analysis
- Actuator integration

### Embedded Systems

- Raspberry Pi 5
- Jetson Nano
- ESP32
- Arduino Mega
- Motors
- Drivers
- Battery power
- Communication between subsystems

### Software & Control

- Python
- C++
- MATLAB
- Simulink
- ROS 2
- Electromechanical control and integration

---

## 🔭 Future Development

Potential future work includes:

- Further mechanical optimisation
- More advanced robotic control
- Expanded sensing and instrumentation
- Improved subsystem communication
- More complete data acquisition
- More extensive validation
- Improved autonomous behaviour
- Detailed inspection-oriented software
- Further industrial feasibility studies

> These points represent **future development directions**, not completed capabilities of the current prototype.

---

## 🧠 Engineering Philosophy

```text
             MECHANICAL ENGINEERING
                       │
                       ▼
              ELECTROMECHANICAL
                 INTEGRATION
                       │
                       ▼
               EMBEDDED SYSTEMS
                       │
                       ▼
                    CONTROL
                       │
                       ▼
                   ROBOTICS
                       │
                       ▼
             INTEGRATED PROTOTYPE
```

> **Engineering is not about building isolated subsystems — it is about making them work together.**

---

## 👥 Project Team

- **Aymane El Haoudar**
- **Mohamed Amine Mohib**
- **Yassine Benkhlouk**
- **Nassim Bouziki**

---

## 👤 About Me

### Aymane El Haoudar

**Electromechanical Engineering Student — Industrial Maintenance & Control**

**ENSAM Meknès · 2024–2028**

My engineering interests combine:

`Mechanical Design` · `Robotics` · `Embedded Systems` · `Automation` · `Industrial Maintenance`

I enjoy engineering projects where mechanical, electrical and software systems have to operate as one integrated architecture.

---

## 🧰 Engineering Skills

```text
MECHANICAL
CATIA V5 • SolidWorks • OpenSCAD • PyCATIA • RDM

EMBEDDED
Raspberry Pi 5 • Jetson Nano • ESP32 • Arduino Mega

PROGRAMMING
Python • C++ • MATLAB • Simulink

ROBOTICS
ROS 2 • Stepper Motors • Servomotors • Kinematics • Control

ENGINEERING
Automation • Electromechanical Integration • Industrial Maintenance
```

---

## 📌 Project Status

<div align="center">

| Area | Status |
|---|---|
| Mechanical Architecture | 🟢 Engineering work |
| Chassis Design | 🟢 Developed |
| Robotic Arm | 🟢 Studied / integrated |
| Embedded Architecture | 🟢 Integrated |
| Motor & Driver Integration | 🟢 Integrated |
| System Communication | 🟢 Engineering integration |
| Industrial Deployment | ⚪ Not claimed |
| Railway Certification | ⚪ Not claimed |

</div>

---

## ⚠️ Technical Disclaimer

RailGard is an **engineering prototype / experimental project**.

This repository does not claim that the system:

- is deployed on operational TGV trains;
- is certified for railway operation;
- is approved for industrial deployment;
- replaces certified railway inspection procedures;
- has completed all validation required for real-world railway operation.

Any future capabilities described in this README are presented as **development directions**, unless explicitly documented as implemented.

---

## 📚 Project Context

The project is based on the **SafeTrack — Robot Autonome d’Inspection Sous-Caisse TGV** engineering work documented in the project portfolio.

The documented technical scope includes mechanical chassis design and dimensioning, multi-axis robotics, embedded platforms, motors/drivers, battery power and communication between subsystems.

---

<div align="center">

### ⚙️ RAILGARD

**Engineering • Robotics • Embedded Systems • Railway Innovation**

<br>

`Design → Integrate → Validate → Improve`

<br>

⭐ If this project interests you, feel free to explore the repository.

</div>
