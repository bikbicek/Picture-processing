import cv2, numpy as np


class Edges:

	def __init__(self, img, edgeColor = (0,0,0)):
		self.img = img

		self.backgroundColor = (0,0,0)
		self.edgeColor = edgeColor
		self.image_Y = self.img.shape[0]
		self.image_X = self.img.shape[1]

		self.threshold = self.imageTreshold(150,240)
		self.edges = self.findEdges(self.threshold)


	def showData(self):
		print("X:",self.image_X," Y:",self.image_Y)
		print("Background color set:",self.backgroundColor)
		print("Edge color set:",self.edgeColor)


	def loadImage(self, path):
		self.img = cv2.imread(path)
		self.image_Y = self.img.shape[0]
		self.image_X = self.img.shape[1]


	def showImage(self):
		cv2.imshow("image",self.img)
		cv2.waitKey()
		cv2.destroyAllWindows()


	def showEdges(self):
		cv2.imshow("image",self.edges)
		cv2.waitKey()
		cv2.destroyAllWindows()


	def showThreshold(self):
		cv2.imshow("image",self.threshold)
		cv2.waitKey()
		cv2.destroyAllWindows()


	def imageTreshold(self, start, end):
		ret,th1 = cv2.threshold(self.img,start,end,cv2.THRESH_BINARY)
		return th1


	def findEdges(self, th1):
		Y,X,Z = th1.shape


		blank_image = np.zeros((Y,X,3), np.uint8)
		blank_image[0:Y,0:X] = (255,255,255)


		t = 20

		lastColor = [255,255,255]

		for x in range(X):
			for y in range(Y):
				s = True
				for color in range(3):
					if lastColor[color] != th1.item(y,x,color):
						lastColor = [th1.item(y,x,0),th1.item(y,x,1),th1.item(y,x,2)]
						blank_image.itemset((y,x,0), self.edgeColor[0])
						blank_image.itemset((y,x,1), self.edgeColor[1])
						blank_image.itemset((y,x,2), self.edgeColor[2])

						s = False
						break
				if s:
					lastColor = [th1.item(y,x,0),th1.item(y,x,1),th1.item(y,x,2)]

		first = True

		for y in range(Y):
			for x in range(X):
				s = True
				for color in range(3):
					if lastColor[color] != th1.item(y,x,color):
						lastColor = [th1.item(y,x,0),th1.item(y,x,1),th1.item(y,x,2)]
						blank_image.itemset((y,x,0), self.edgeColor[0])
						blank_image.itemset((y,x,1), self.edgeColor[1])
						blank_image.itemset((y,x,2), self.edgeColor[2])
						s = False

						break
				if s:
					lastColor = [th1.item(y,x,0),th1.item(y,x,1),th1.item(y,x,2)]

		return blank_image
