import cv2
import pygame
from cv2 import threshold
cam = cv2.VideoCapture(0)

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("ocean.mp3")

while cam.isOpened():
    ret, frame0 = cam.read()
    ret, frame1 = cam.read()
    diff = cv2.absdiff(frame0, frame1)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0,255,150), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,100), 2)
        sound.play()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('ATZ', frame1)

