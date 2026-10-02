# Interfaces and Communication

| From | To | Interface / Protocol | Intended role |
|---|---|---|---|
| Raspberry Pi | ESP32 | Wi-Fi / LoRa | Commands and sensor data |
| ESP32 | Motors | PWM / GPIO | Speed and direction control |
| ESP32 | Sensors | UART / I2C / SPI | Data acquisition |
| Camera | Raspberry Pi | CSI / USB | Image acquisition |
| LiDAR | Controller | Interface specified by implementation | Navigation / obstacle data |
| Raspberry Pi | User interface | WebSocket / Bluetooth / LoRa concepts | Operator communication |

## Implementation note

The table is a repository documentation baseline derived from the technical
dossier. It is not proof that every listed interface was physically
implemented in the final prototype.

Replace an entry with measured/implemented details when the corresponding
schematic, source code, or test evidence is added.
