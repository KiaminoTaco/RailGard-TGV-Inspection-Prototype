from pathlib import Path
import time

from picamera import PiCamera


OUTPUT_DIR = Path("/home/pi/Pictures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

camera = PiCamera()
try:
    time.sleep(2)
    camera.resolution = (1280, 720)
    camera.vflip = True
    camera.contrast = 10

    file_name = OUTPUT_DIR / f"img_{time.time():.6f}.jpg"
    camera.capture(str(file_name))
    print(f"Image captured: {file_name}")
finally:
    camera.close()
