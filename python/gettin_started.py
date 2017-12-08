import cv2

camera = cv2.VideoCapture(0)

window_name = "My Window"

cv2.namedWindow(window_name)

read_ok, frame = camera.read()

while read_ok and cv2.waitKey(1) != ord('s'):
	cv2.imshow(window_name, frame)
	read_ok, frame = camera.read()

camera.release()
cv2.destroyAllWindows()	
