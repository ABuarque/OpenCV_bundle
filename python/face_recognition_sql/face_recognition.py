import cv2
import numpy as np
import sqlite3

# model to train classifiear
front_face_model = "../resources/haarcascade_frontalface_default.xml"

# face detector 
face_detect = cv2.CascadeClassifier(front_face_model)

# getting webcam
camera = cv2.VideoCapture(0)

counter = 0

def insert_or_update(id, name):
	connection = sqlite3.connect("FaceBase")
	query = "select * from People where ID=" + str(id)
	cursor = connection.execute(query)
	is_record_exist = False
	for row in cursor:
		is_record_exist = True
	if(is_record_exist): # update
		query = "UPDATE people SET Name=' "+str(name)+" ' WHERE ID="+str(id)
	else:
		query = "INSERT INTO people(ID,Name) Values("+str(id)+",' "+str(name)+" ' )"
	connection.execute(query)
	connection.commit()
	connection.close()

identifier = input("Enter user id: ")
name = input("Enter user name: ")

insert_or_update(identifier, name)

while(True):
	ret, image = camera.read() # status and frame

	# classifier requires grayscale image, to lets parse it
	grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# get faces and return its points
	faces = face_detect.detectMultiScale(grayscale_image, 1.3, 5)
	for (x, y, z, h) in faces:
		counter += 1
		cv2.imwrite("data_set/User.{}.{}.jpg"
			.format(identifier, counter), grayscale_image[y:y + h, x:x + z])
		cv2.rectangle(image, (x, y), (x + z, y + h), (255,0,0), 2)
		cv2.waitKey(100)

	cv2.imshow("Face", image)
	cv2.waitKey(1)
	if(counter > 20):
		break

camera.release()
cv2.destroyAllWindows()


