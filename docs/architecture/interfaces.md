# Interfaces and Communication

| From | To | Interface / Protocol | Intended role |
|---|---|---|---|
| Raspberry Pi | ESP32 | Wi-Fi / LoRa | Commands and sensor data |
| ESP32 | Motors | PWM / GPIO | Speed and direction control |
| ESP32 | Sensors | UART / I2C / SPI | Data acquisition |
| Camera | Raspberry Pi | CSI / USB | Image acquisition |
| LiDAR | Controller | Interface specified by implementation | Navigation / obstacle data |
| Raspberry Pi | User interface | WebSocket / Bluetooth / LoRa concepts | Operator communication |
