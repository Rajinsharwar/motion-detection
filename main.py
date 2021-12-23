import cv2
import pygame
pygame.init()
# pygame.mixer.init()
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, framenum1 = camera.read()
    ret, framenum2 = camera.read()
    difference = cv2.absdiff(framenum1, framenum2)
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilatedimg = cv2.dilate(thresh, None, iterations=3)
    contoursframe, _ = cv2.findContours(dilatedimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contoursframe:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(framenum1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        alert = pygame.mixer.Sound('alert.wav')
        alert.play()
        # Exiting Button
    if cv2.waitKey(10) == ord('x'):
        break
    cv2.imshow('Rajin Traffic Cam', framenum1)