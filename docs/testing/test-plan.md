# Prototype Test Plan

This is a documentation framework for future or ongoing validation. It does
not claim that the tests below have already been completed.

## 1. Mechanical

### Chassis
- Verify dimensions against the design.
- Verify assembly of structural elements.
- Check mass and centre-of-gravity assumptions.

### Robotic arm
- Verify axis movement.
- Verify actuator direction.
- Verify torque assumptions.
- Check mechanical interference.

## 2. Electronics

- Verify supply rails.
- Verify controller startup.
- Verify motor-driver connections.
- Verify sensor communication.
- Verify emergency/stop behaviour where implemented.

## 3. Embedded software

- Verify command reception.
- Verify motor control.
- Verify sensor acquisition.
- Verify communication between controller layers.

## 4. Navigation / sensing

- Verify LiDAR data acquisition.
- Verify obstacle detection.
- Verify camera acquisition.
- Verify ultrasonic/infrared sensing where implemented.

## 5. System integration

Record:

- test date;
- hardware revision;
- software revision;
- test conditions;
- expected result;
- observed result;
- pass/fail;
- evidence;
- corrective action.

## Important

Do not mark a test as passed without evidence.
