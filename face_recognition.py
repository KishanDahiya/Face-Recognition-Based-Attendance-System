from tkinter import *
from tkinter import ttk #stylish GUI
from PIL import Image,ImageTk #for images
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from time import strftime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        img_left=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\face_detect.jpg")
        img_left=img_left.resize((683,700),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=35,width=683,height=700)

        img_right=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\phone.jpg")
        img_right=img_right.resize((683,700),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=683,y=35,width=683,height=700)

        b1_1=Button(f_lbl,text="Give Attendance",command=self.face_recog,font=("times new roman",20,"bold"),cursor="hand2",bg="lightblue",fg="black")
        b1_1.place(x=190,y=460,width=230,height=35)
    
    
    #Marking attendance function
    def mark_attendance(self,i,n,c,s):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (c not in name_list) and (s not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{c},{s},{dtString},{d1},Present")
                
    #Recognizing face function
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
                my_cursor=conn.cursor()

                my_cursor.execute("select roll from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select course from student where student_id="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)

                my_cursor.execute("select semester from student where student_id="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)
                
                if confidence>77:
                    cv2.putText(img,f"USN:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Course:{c}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Sem:{s}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,n,c,s)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Face\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Face\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()