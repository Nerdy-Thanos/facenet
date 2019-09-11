import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("datasets/vignesh0/1.jpg")

grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img,scaleFactor = 1.05,minNeighbors=5)

for x,y,w,h in faces:
	cropped=img[y:y+h,x:x+w]
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
	resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
	cv2.imwrite('1.jpg',cropped)

cv2.imshow("GRAY",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
