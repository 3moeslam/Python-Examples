'''
Created on Dec 4, 2017

@author: Eslam
'''

import cv2
#Read Image
img = cv2.imread('img.png')
#Get Image Shape
height, width, channels = img.shape
#print Image Shape
print "Height: {0} , Width: {1}, Channels: {2}".format(height,width,channels)