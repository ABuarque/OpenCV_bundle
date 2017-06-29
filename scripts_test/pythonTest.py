import cv2

#global flag to turn off app
clicked = False

#callback functuon to handle when mouse left button is clicked
def onMouse(event, x, y, flags, param):
	global clicked #referencing the clicked
	if event == cv2.EVENT_LBUTTONUP: # check left button clicked
		clicked = True

#creating a videoCapture obj
cameraCapture = cv2.VideoCapture(0)

#creating a window and putting a name
cv2.namedWindow("my window")

#setting the call callback function for the created window
cv2.setMouseCallback("my window", onMouse) 

print("Click to stop shoting")

#reading frames and if it's ok
sucess, frame = cameraCapture.read()
while sucess and cv2.waitKey(1) == -1 and not clicked:
	cv2.imshow("my window", frame)
	sucess, frame = cameraCapture.read()