import argparse
from pathlib import Path

import cv2


def detect_objects(image_path: Path, cascade_path: Path):
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    classifier = cv2.CascadeClassifier(str(cascade_path))
    if classifier.empty():
        raise FileNotFoundError(
            f"Cannot load Haar cascade: {cascade_path}"
        )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    objects = classifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
    )

    for x, y, w, h in objects:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2,
        )

    return image, objects


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("cascade", type=Path)
    args = parser.parse_args()

    result, objects = detect_objects(args.image, args.cascade)
    print(f"Detected objects: {len(objects)}")

    cv2.imshow("Detected Objects", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
