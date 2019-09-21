import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import dlib
import os                                                                       # for creating folders

cap = cv2.VideoCapture('video_for_training.mp4')
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()


def insert_update(Id, name, roll_no) :    

    connect = sqlite3.connect("face_dataBase.db")
    c = connect.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS student(
    ID integer,
    name text,
    roll_no integer
    )""")


    cmd = "SELECT * FROM student WHERE ID = " + Id                             # selecting the row of an id to check
    d = c.execute(cmd)
    if_present = 0
    for r in d:
        print("yes record present")                                                          
        if_present = 1
    if if_present == 1:                                                      
        c.execute("UPDATE student SET name = ? WHERE ID = ?",(name, Id))
        c.execute("UPDATE student SET roll_no = ? WHERE ID = ?",(roll_no, Id))
    else:                                               
    	c.execute("INSERT INTO student VALUES(?, ?, ?)", (Id, name, roll_no))

    c.execute("SELECT * FROM student")
    print(c.fetchall())
    connect.commit()                                                            
    connect.close()


Id = input("Enter your ID: ")
name = input("Enter your NAME: ")
roll_no = input("Enter your ROLL_NO: ")

insert_update(Id, name, roll_no)

# c.execute("INSERT INTO student VALUES(?,?,?)",(Id, name, roll_no))



folderName = "student" + Id                                                        # creating the person or user folder
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

sampleNum = 0
while(True):
    ret, img = cap.read()                                                       
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                
    dets = detector(img, 1)
    for i, d in enumerate(dets):                                                
        sampleNum += 1
        cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                    img[d.top():d.bottom(), d.left():d.right()])                                                
        cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) 
        cv2.waitKey(100)                                                        
    cv2.imshow('frame', img)                                                    
    cv2.waitKey(1)
    if(sampleNum >= 20):                                                        
        break

cap.release()                                                                   
cv2.destroyAllWindows()                                                         


