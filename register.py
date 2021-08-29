from tkinter import* 
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import connection

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x700+0+0")

        #variables to store data
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        #Background Image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\bg.jpg")
        bg_lbl1=Label(self.root,image=self.bg1)
        bg_lbl1.place(x=0,y=0,relwidth=1,relheight=1)

        #Left Image
        self.bg2=ImageTk.PhotoImage(file=r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\left.jpg")
        bg_lbl2=Label(self.root,image=self.bg2)
        bg_lbl2.place(x=50,y=80,width=470,height=550)

        #Frame for Register box
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=80,width=800,height=550)

        #Text in Register Now frame
        register_lbl=Label(frame,text="Register Now !!!",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=10)

        #Labels in Register Frame

        #left row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=20,y=50)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=20,y=80,width=250)
       
        #right row 1
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=350,y=50)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=350,y=80,width=250)

        #left row 2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=20,y=115)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=20,y=145,width=250)
        
        #right row 2
        email=Label(frame,text="E-mail/Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=350,y=115)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=350,y=145,width=250)

        #left row 3
        security_q=Label(frame,text="Select security question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_q.place(x=20,y=175)
        #setting up combobox on left
        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",14),state="readonly")
        self.combo_security_q["values"]=("Click To Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
        self.combo_security_q.place(x=20,y=205,width=250)
        self.combo_security_q.current(0)

        #right row 3
        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=350,y=175)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=350,y=205,width=250)

        #left row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=20,y=240)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=20,y=265,width=250)

        #right row 4
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=350,y=240)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=350,y=265,width=250)

        #Check Button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms And Conditions",font=("times new roman",12),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=20,y=300)

        #Buttons 

        #register button
        img=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\register.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"),bg="white")
        b1.place(x=20,y=330,width=200)

        #login button
        img1=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\login.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",14,"bold"),bg="white")
        b2.place(x=350,y=330,width=200)


    #Action on Register button
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All feilds are required !!!",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password Mismatch",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree To Terms And Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist's , Please Try Another E-Mail")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registeration successfull",parent=self.root)

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
