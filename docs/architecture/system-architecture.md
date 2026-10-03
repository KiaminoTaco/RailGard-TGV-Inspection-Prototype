# System Architecture

## 1. High-level architecture

The project architecture is organized around three engineering layers:

1. Mechanical architecture
2. Embedded electronics
3. Robotics and control

These layers are integrated through motors, actuators, communication and
data acquisition.

## 2. Embedded architecture

The technical dossier identifies a master/slave concept:

### Master — Raspberry Pi 5

Documented roles include:

- coordination of communications;
- processing sensor information;
- camera/image processing;
- higher-level control and decision logic;
- communication with the embedded controller;
- local data handling.

### Embedded controller — ESP32

Documented roles include:

- motor command execution;
- sensor management;
- reception of commands from the higher-level computer;
- transmission of sensor information.

The dossier also discusses Arduino/Teensy-based control concepts in different
sections. The exact final controller allocation should therefore be kept
consistent with the actual hardware/code committed to the repository.

## 3. Main sensing elements

The technical dossier describes:

- Raspberry Pi Camera Module 3;
- RPLIDAR A3M1;
- SRF10 ultrasonic sensing;
- LM35 temperature sensing;
- Sharp GP2Y0A02YK0F infrared distance sensing;
- IMU;
- LoRa communication modules.

## 4. Actuation

The documented architecture includes:

- stepper motors;
- DC motors;
- servomotors;
- geared motors;
- A4988 stepper drivers;
- L298N motor driver.

## 5. Communication

The dossier describes communication using combinations of:

- Wi-Fi;
- LoRa;
- UART;
- I2C;
- SPI;
- GPIO;
- MQTT/WebSocket/Bluetooth concepts for interfaces.

