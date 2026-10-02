from pathlib import Path

import cv2


def latest_image(directory: Path) -> Path:
    images = sorted(
        directory.glob("img_*.jpg"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not images:
        raise FileNotFoundError(f"No img_*.jpg found in {directory}")
    return images[0]


def detect_differences(reference_path: Path, captured_path: Path, threshold: int = 50):
    reference = cv2.imread(str(reference_path))
    captured = cv2.imread(str(captured_path))

    if reference is None:
        raise FileNotFoundError(f"Cannot read reference image: {reference_path}")
    if captured is None:
        raise FileNotFoundError(f"Cannot read captured image: {captured_path}")

    if reference.shape[:2] != captured.shape[:2]:
        captured = cv2.resize(
            captured,
            (reference.shape[1], reference.shape[0]),
        )

    ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    cap_gray = cv2.cvtColor(captured, cv2.COLOR_BGR2GRAY)

    diff_img = cv2.absdiff(ref_gray, cap_gray)
    _, diff_img = cv2.threshold(
        diff_img,
        threshold,
        255,
        cv2.THRESH_BINARY,
    )

    contours, _ = cv2.findContours(
        diff_img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    result = captured.copy()
    boxes = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        boxes.append((x, y, w, h))
        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2,
        )

    return result, diff_img, boxes


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, default=Path("ref_img.jpg"))
    parser.add_argument("--image", type=Path)
    parser.add_argument("--directory", type=Path, default=Path("."))
    parser.add_argument("--threshold", type=int, default=50)
    args = parser.parse_args()

    image_path = args.image or latest_image(args.directory)

    result, _, boxes = detect_differences(
        args.reference,
        image_path,
        args.threshold,
    )

    print(f"Detected regions: {len(boxes)}")

    cv2.imshow("Captured Image - Detected Differences", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
