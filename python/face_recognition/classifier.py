import os
import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = "data_set"

def get_images_id(path):
	image_paths = [os.path.join(path, files) for files in os.listdir()]
	print(image_paths)

get_images_id(path)
