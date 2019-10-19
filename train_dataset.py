import cv2
import os
import numpy as np

path ='./dataset'

def images_with_id(path):
    img_folders = [os.path.join(path,f) for f in os.listdir(path)]

    faces = []
    ids = []

    for img_folder in img_folders:
        reg_no = os.path.split(img_folder)[1]
        reg_no = int(reg_no.replace("student",""))
        # print(img_folder)
        print(reg_no)
        images_path = [os.path.join(img_folder,im) for im in os.listdir(img_folder)]
        for image_path in images_path:
            print(image_path)
            image = cv2.imread(image_path)
            cv2.imshow("Training on image...", image)
            cv2.waitKey(10)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces.append(gray)
            ids.append(reg_no)

    return faces, ids


faces, ids = images_with_id(path)
print("Total faces: ", len(faces))
print("Total IDs: ", len(ids))

# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.train(faces, np.array(ids))
# 
# face = cv2.imread("test.jpg")
# face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
# label, confidence = face_recognizer.predict(face)
# print("Level of confidence: ", confidence)
# print(label)