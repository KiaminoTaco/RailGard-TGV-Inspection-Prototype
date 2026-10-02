# Electronics and Power Architecture

## Main embedded platforms

The technical dossier discusses:

- Raspberry Pi 5;
- ESP32;
- Arduino/embedded controller concepts;
- motor drivers;
- battery power.

## Sensors

The documented sensing architecture includes:

- Camera Module 3;
- RPLIDAR A3M1;
- SRF10 ultrasonic sensor;
- LM35 temperature sensor;
- Sharp GP2Y0A02YK0F infrared sensor;
- IMU.

## Motor and actuator interfaces

The dossier identifies:

- A4988 stepper motor drivers;
- L298N motor driver;
- stepper motors;
- DC motors;
- servomotors;
- geared motors.

## Power

The dossier contains separate power-consumption and battery-sizing studies.
Keep the original calculations in `electronics/power/` and do not replace
engineering calculations with generic estimates.

## Repository rule

Every electrical diagram committed to this repository should identify:

- supply voltage;
- ground/reference;
- controller;
- driver;
- actuator/sensor;
- communication interface;
- protection elements where documented.
