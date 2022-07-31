from django.test import TestCase
import cv2

# Create your tests here.
data = cv2.imread('static/img/25.jpg')
test = cv2.imread('static/img/hongwen.jpg')
data = cv2.resize(data, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
test = cv2.resize(test, dsize=(1024, 1024), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
result = data & test
cv2.imshow('data', result)
cv2.waitKey(0)
