import face_recognition
import cv2
import numpy as np
import encoding

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    img_resize = cv2.resize(image, (0, 0), None, 0.25, 0.25)
    img_resize = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
    faces_video = face_recognition.face_locations(img_resize)
    live_encoding = face_recognition.face_encodings(img_resize, faces_video)
    for encode_face, faceloc in zip(live_encoding, faces_video):


