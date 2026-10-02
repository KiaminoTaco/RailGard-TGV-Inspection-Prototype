import cv2

# Load the Haar cascades classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture image using Raspberry Pi camera
cap_img = cv2.imread('img_*.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.1,
    minNeighbors=5
)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(cap_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the captured image with the detected faces
cv2.imshow('Captured Image', cap_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
