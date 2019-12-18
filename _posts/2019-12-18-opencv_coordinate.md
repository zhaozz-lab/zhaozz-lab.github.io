---
layout: post
title: "opencv coordinate"
categories: opencv
---

## opencv coordinate
In using opencv,the order of the image shape is (height,width,channel),but when draw circle or line,the first ordinate is the (x,y),the x is horizon and y is vertical.

```python
import cv2
image_name = "1.jpg"
img = cv2.imread(image_name)
x,y = 10,100
cv2.circle(img, (x, y), 10, (0, 255, 0), -1))
``` 