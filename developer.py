from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Developer")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        img_right=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\right.jpg")
        img_right=img_right.resize((1366,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_right)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=0,y=35,width=1366,height=700)
        
        #---------------------------right side developer info frame------------------------------------------
        devs_frame=Frame(bg_img,bd=2,bg="white")
        devs_frame.place(x=1000,y=0,width=366,height=700)

        img_in_devs=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\dev.png")
        img_in_devs=img_in_devs.resize((180,180),Image.ANTIALIAS)
        self.photoimg_in_devs=ImageTk.PhotoImage(img_in_devs)

        devs_img=Label(devs_frame,image=self.photoimg_in_devs,background="white")
        devs_img.place(x=91,y=20,width=180,height=180)

        #----------------------------------------Developers info-----------------------------------------------
        right_inside_frame=Frame(devs_frame,bd=2,relief=RIDGE,bg="white")
        right_inside_frame.place(x=10,y=210,width=340,height=450)

        title_lbl=Label(right_inside_frame,text="DEVELOPER INFO",font=("times new roman",20,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=340,height=30)

        dev_label=Label(right_inside_frame,text="Hello, I am Kishan Dahiya.",bg="white",font=("Times new roman",12,"bold"))
        dev_label.place(x=0,y=30)

        dev_label1=Label(right_inside_frame,text="Ph : +91-797-748-4702",bg="white",font=("Times new roman",12,"bold"))
        dev_label1.place(x=0,y=50)

        dev_label2=Label(right_inside_frame,text="E-mail : kkd999.km@gmail.com",bg="white",font=("Times new roman",12,"bold"))
        dev_label2.place(x=0,y=70)

        img_in_devs1=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\student.png")
        img_in_devs1=img_in_devs1.resize((300,300),Image.ANTIALIAS)
        self.photoimg_in_devs1=ImageTk.PhotoImage(img_in_devs1)

        devs_img=Label(right_inside_frame,image=self.photoimg_in_devs1,background="white")
        devs_img.place(x=20,y=120,width=300,height=300)

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()