import cv2
import sys
import os
import platform

#image and haarcascade file
imagePath = sys.argv[1]
userHome = os.path.expanduser('~')
userDesktop = userHome + '/Desktop/'
fileName = 'FaceDetected-OUT.jpg'
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

image = cv2.imread(imagePath)
#convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#parameters need to be adjusted on a case by case basis
faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.2,
	minNeighbors=5,
	minSize=(30,30),
	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces".format(len(faces))

#Draw rectangle around faces
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite(userDesktop + fileName, image)
