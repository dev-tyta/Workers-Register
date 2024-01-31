import cv2
import face_recognition

image = face_recognition.load_image_file("../../data/player_data/faruq.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

face_locations = face_recognition.face_locations(imagge)[0]
img_copy = image.copy()

cv2.rectangle(img_copy, (face_locations[3], face_locations[0]), (face_locations[2], face_locations[1]), (0, 255))
cv2.imshow("bgr", img_copy)
cv2.waitKey(0)
