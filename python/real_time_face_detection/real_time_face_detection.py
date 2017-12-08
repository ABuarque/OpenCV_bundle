import cv2
import numpy as np

# model to train classifiear
front_face_model = "../resources/haarcascade_frontalface_default.xml"

# face detector 
face_detect = cv2.CascadeClassifier(front_face_model)

# getting webcam
camera = cv2.VideoCapture(0)

while(True):
	ret, image = camera.read() # status and frame

	# classifier requires grayscale image, to lets parse it
	grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# get faces and return its points
	faces = face_detect.detectMultiScale(grayscale_image, 1.3, 5)
	for (x, y, z, h) in faces:
		cv2.rectangle(image, (x, y), (x + z, y + h), (255,0,0), 2)

	cv2.imshow("Face", image)
	if(cv2.waitKey(1) == ord('q')): # if hit q, exit loop
		break

camera.release()
cv2.destroyAllWindows()

