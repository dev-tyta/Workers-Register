import cv2
import face_recognition
from ..data.preprocess_data import preprocess

file_path = "../../data/player_data"


def encode_faces(path):
    encodings = []
    images, img_name = preprocess(path)
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodings.append(encoded_face)
    return encodings


# testing function
encoding_face = encode_faces(file_path)
