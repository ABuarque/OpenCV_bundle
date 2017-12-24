import cv2
import numpy as np
import sqlite3

# model to train classifiear
front_face_model = "../resources/haarcascade_frontalface_default.xml"

# face detector 
face_detect = cv2.CascadeClassifier(front_face_model)

# getting webcam
camera = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("recognizer/training_data.yml")

def get_profile(id):
	connection = sqlite3.connect("FaceBase")
	query = "SELECT * FROM People WHERE ID=" + str(id)
	cursor = connection.execute(query)
	profile = None
	for row in cursor:
		profile = row

	connection.close()
	return profile

id = 0

font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
	ret, image = camera.read() # status and frame

	# classifier requires grayscale image, to lets parse it
	grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# get faces and return its points
	faces = face_detect.detectMultiScale(grayscale_image, 1.3, 5)
	for (x, y, z, h) in faces:
		cv2.rectangle(image, (x, y), (x + z, y + h), (255,0,0), 2)

		id, configuration = recognizer.predict(grayscale_image[y:y + h,x:x + z])
		
		profile = get_profile(id)
		if(profile is not None):
			cv2.putText(image, str(profile[0]), (x, y+h + 30),font,1,(255,0,0),3);
			cv2.putText(image, str(profile[1]), (x, y+h + 60),font,1,(255,0,0),3);
			cv2.putText(image, str(profile[2]), (x, y+h + 90),font,1,(255,0,0),3);
			cv2.putText(image, str(profile[3]), (x, y+h + 120),font,1,(255,0,0),3);
			cv2.putText(image, str(profile[4]), (x, y+h + 150),font,1,(255,0,0),3);

	cv2.imshow("Face", image)
	if(cv2.waitKey(1) == ord('q')): # if hit q, exit loop
		break

camera.release()
cv2.destroyAllWindows()

