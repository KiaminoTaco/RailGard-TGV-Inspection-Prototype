import argparse
from io import BytesIO
from pathlib import Path

import numpy as np
import requests
import tensorflow as tf
from PIL import Image


def load_image_from_url(url: str) -> tf.Tensor:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content)).convert("RGB")
    image = np.asarray(image)

    return tf.convert_to_tensor(image, dtype=tf.float32)


def predict_anomaly(model_path: Path, image: tf.Tensor, threshold: float = 0.5):
    model = tf.keras.models.load_model(model_path)

    image = tf.image.resize(image, (224, 224))
    image = image / 255.0

    predictions = model.predict(
        tf.expand_dims(image, axis=0),
        verbose=0,
    )

    score = float(np.asarray(predictions).reshape(-1)[0])
    is_anomaly = score > threshold

    return score, is_anomaly


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("image_url")
    parser.add_argument("--threshold", type=float, default=0.5)
    args = parser.parse_args()

    image = load_image_from_url(args.image_url)
    score, is_anomaly = predict_anomaly(
        args.model,
        image,
        args.threshold,
    )

    print(f"Anomaly score: {score:.4f}")

    if is_anomaly:
        print("Anomalie détectée sur la bougie du train. Alerte envoyée.")
    else:
        print("Aucune anomalie détectée au-dessus du seuil.")
