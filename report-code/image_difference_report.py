import cv2
import numpy as np

# Load reference image
ref_img = cv2.imread('ref_img.jpg')
ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)

# Capture image using Raspberry Pi camera
cap_img = cv2.imread('img_*.jpg')
cap_gray = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)

# Subtract the reference image from the captured image
diff_img = cv2.absdiff(ref_gray, cap_gray)

# Apply thresholding to the difference image
threshold = 50
_, diff_img = cv2.threshold(diff_img, threshold, 255, cv2.THRESH_BINARY)

# Find contours in the difference image
contours, _ = cv2.findContours(
    diff_img,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw rectangles around the detected differences
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(cap_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the captured image with the detected differences
cv2.imshow('Captured Image', cap_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
