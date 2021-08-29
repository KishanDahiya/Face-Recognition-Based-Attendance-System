import os
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Auto-Log Attendance")

        img=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\dat_train.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        img1=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\dat_train.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)

        img2=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\dat_train.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=470,height=130)

        #background Image
        img3=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\bg.jpg")
        img3=img3.resize((1366,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=700)
        
        title_lbl=Label(bg_img,text="AUTO-LOG ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=47)

        #Student Button
        img4=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\student.png")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=80,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=120,y=260,width=180,height=30)

        #Detect Face Button
        img5=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\face_detect.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=440,y=80,width=180,height=180)

        b1_1=Button(bg_img,text="Mark Attendance",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=440,y=260,width=180,height=30)

        #Attendance Button
        img6=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\att.png")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b1.place(x=740,y=80,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=740,y=260,width=180,height=30)

        #Help Button
        img7=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\help.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1040,y=80,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=1040,y=260,width=180,height=30)

        #Train Button
        img8=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\train.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=120,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=120,y=530,width=180,height=30)

        #Photos(Gallery) Button
        img9=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\photos.png")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=440,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Collected Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=440,y=530,width=180,height=30)

        #Developer Button
        img10=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\dev.png")
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer)
        b1.place(x=740,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=740,y=530,width=180,height=30)

        #exit Button
        img11=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\exit.png")
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.i_exit)
        b1.place(x=1040,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.i_exit,font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=1040,y=530,width=180,height=30)

    #Photos (Gallery) button
    def open_img(self):
        os.startfile(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Face\data")
    
    def i_exit(self):
        self.i_exit=messagebox.askyesno("Auto-Log Attendance","Are you sure to exit?",parent=self.root)
        if self.i_exit>0:
            self.root.destroy()
        else:
            return

    #Function Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()