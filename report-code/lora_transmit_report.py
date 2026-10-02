import socket
import time

# Initialize LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DRATE_REGION, 1)
s.setsockopt(socket.SOL_LORA, socket.SO_LORA_BANDWIDTH, 0)  # 125 kHz
s.setsockopt(socket.SOL_LORA, socket.SO_LORA_SPREADING_FACTOR, 7)  # 6-12
s.setsockopt(socket.SOL_LORA, socket.SO_LORA_CODING_RATE, 4)  # 4/5
s.setsockopt(socket.SOL_LORA, socket.SO_LORA_PREAMBLE, 8)  # Default
s.setsockopt(socket.SOL_LORA, socket.SO_LORA_IQ, 0)  # Default

# Open a LoRa socket
s.bind(1)

# Transmit captured image
with open('img_*.jpg', 'rb') as f:
    data = f.read()
    s.send(data)
    print("Image sent!")

# Close the socket
s.close()
