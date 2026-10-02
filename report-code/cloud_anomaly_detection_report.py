import tensorflow as tf
import numpy as np
import requests

# Load an AI model for anomaly detection
model = tf.keras.models.load_model('anomaly_detection_model.h5')

# Load an image from the cloud (example)
image_data = requests.get(
    "https://Train-cloud.com/Anomalies_data.jpg"
)
image = np.array(image_data.content)

# Preprocess the image (resize, normalize, etc.)
image = tf.image.resize(image, (224, 224))
image = image / 255.0

# Prediction of the anomaly
predictions = model.predict(
    np.expand_dims(image, axis=0)
)

# If anomaly probability exceeds a threshold, alert maintenance
if predictions[0] > 0.5:
    print("Anomalie détectée sur la bougie du train. Alerte envoyée.")
