import cv2, numpy as np
from edges import Edges

x = Edges(cv2.imread("picture.png"), (0,0,255))
x.showData()
cv2.imwrite("hue.jpg",x.edges)
x.showThreshold()
x.showEdges()   