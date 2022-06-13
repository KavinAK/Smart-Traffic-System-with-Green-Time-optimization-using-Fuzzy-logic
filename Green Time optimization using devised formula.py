from platform import python_version
import tensorflow
import keras
import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
from cv2 import *


def getObjects(img, speedLimit, CrossingLength):
    bbox, label, conf = cv.detect_common_objects(img)
    draw_bbox(img, bbox, label, conf)
    print(label.count('car') + label.count('motorcycle') + label.count('truck'))
    
    speedLimit1 = (speedLimit*5)/18

    K1 = (CrossingLength + 1.5)/speedLimit1
    K2 = (CrossingLength + 3)/speedLimit1
    K3 = (CrossingLength + 5)/speedLimit1

    G = 2 + (K1*label.count('motorcycle'))/4 + (K2*label.count('car'))/2 + (K3*label.count('truck'))/2 + K3
    print(G)
    return img

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    
    speedLimit = float(input("Enter number "))
    CrossingLength = float(input("Enter number "))
    result, img = cap.read()
    result = getObjects(img, speedLimit, CrossingLength)
    #cv2.imwrite("C:\\Users\\Kalaikumar\\Downloads\\NumberoffVehicles.png", img)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
