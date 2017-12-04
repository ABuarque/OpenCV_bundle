import cv2

image_path = "moza1.jpg" # used image

cascace_path = "resources/haarcascade_frontalface_default.xml" # model for frontal face

classifier = cv2.CascadeClassifier(cascace_path) # creating a classifier for frontal face

image = cv2.imread(image_path) # reading the iamge

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # parsing image to gray scale
 
faces = classifier.detectMultiScale(gray_image, 2.5, 10) # gettins all the faces in image

for (x, y, z, h) in faces: # for each face...
	image = cv2.rectangle(image, (x, y) , (x + z, y + h), (255, 255, 0), 2) # make a rectangle

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
