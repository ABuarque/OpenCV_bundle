import os
import cv2
import numpy as np
#from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = "data_set"

def get_images_with_id(path):
	image_paths = [os.path.join(path, files) for files in os.listdir(path)]

	faces = []
	IDs = []

	for image_path in image_paths:
		#face_img = Image.open(image_path).convert("L")
		face_img = cv2.imread(image_path, 0) # opens up in grayscale
		np_face = np.array(face_img, "uint8") # created numpy array

		ID = int(os.path.split(image_path)[-1].split(".")[1])

		faces.append(np_face)
		IDs.append(ID)

		cv2.imshow("training", np_face)
		cv2.waitKey(10)
	return np.array(IDs), faces

Ids, faces = get_images_with_id(path)

recognizer.train(faces, Ids)
recognizer.write("recognizer/training_data.yml")

cv2.destroyAllWindows()



