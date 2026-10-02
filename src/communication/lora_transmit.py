import argparse
import socket
from pathlib import Path


def send_image(image_path: Path):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    try:
        s.setsockopt(socket.SOL_LORA, socket.SO_DRATE_REGION, 1)
        s.setsockopt(socket.SOL_LORA, socket.SO_LORA_BANDWIDTH, 0)
        s.setsockopt(socket.SOL_LORA, socket.SO_LORA_SPREADING_FACTOR, 7)
        s.setsockopt(socket.SOL_LORA, socket.SO_LORA_CODING_RATE, 4)
        s.setsockopt(socket.SOL_LORA, socket.SO_LORA_PREAMBLE, 8)
        s.setsockopt(socket.SOL_LORA, socket.SO_LORA_IQ, 0)

        s.bind(1)

        with image_path.open("rb") as f:
            data = f.read()

        s.send(data)
        print(f"Image sent: {image_path}")
    finally:
        s.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    args = parser.parse_args()

    send_image(args.image)
