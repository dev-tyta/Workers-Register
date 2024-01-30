import cv2
import numpy as np
import face_recognition

image_bgr = face_recognition.load_image_file("../../data/player_data/bim.png")
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

cv2.imshow("bim_rgb", image_rgb)
cv2.imshow("bim_bgr", image_bgr)
cv2.waitKey(0)
