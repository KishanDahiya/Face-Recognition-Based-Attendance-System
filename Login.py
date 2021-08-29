from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x700+0+0")
        
        #Background Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\bg.jpg") #Background of login page
        lbl_bg=Label(self.root,image=self.bg) #window space for login
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Frame for Login box
        frame=Frame(self.root,bg="black")
        frame.place(x=535,y=130,width=350,height=450)

        #User icon on login form
        img1=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\User.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=660,y=138,width=100,height=100)

        #Startup Text
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=105,y=105)

        #Label after Username
        username=lbl=Label(frame,text="E-mail / Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",20))
        self.txtuser.place(x=40,y=180,width=270)

        #Label for Password
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=239)
        self.txtpass=ttk.Entry(frame,font=("times new roman",20))
        self.txtpass.place(x=40,y=270,width=270)

        #Icon near Username Text
        img2=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\User.png") #user icon for login
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=282,width=25,height=25)

        #Icon near Password Text
        img3=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\User.png") #user icon for login
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=372,width=25,height=25)

        #Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="Red")
        loginbtn.place(x=98,y=320,width=150,height=35)

        #New Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=365,width=300)

        #Forgot password Button
        passwordbtn=Button(frame,text="Forgot Password ?",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        passwordbtn.place(x=20,y=390,width=300)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get=='' or self.txtpass.get=='':
            messagebox.showerror("Error","All fields required",parent=self.root)
        elif self.txtuser.get()=="kishan" and self.txtpass.get()=='1234':
            messagebox.showinfo("Success","Welcome !!!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username And Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("Yes or No","Access only to Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    #self.app=Face_Recognition_System(self.new_window)
                    pass
                else:
                    if not open_main:
                        messagebox.showerror("Error","Non Authorized personnal not allowed.",parent=self.root)
                        return
            conn.commit()
            conn.close()

    #reset password button block
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question !!!",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer.",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password.",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer.",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password Reset successfull",parent=self.root2)
                self.root2.destroy()

    #forgot password block
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the e-mail address/username to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+540+150")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=10,y=10,relwidth=1)

                security_q=Label(self.root2,text="Select security question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_q.place(x=30,y=80)
                #setting up combobox 
                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",14),state="readonly")
                self.combo_security_q["values"]=("Click To Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
                self.combo_security_q.place(x=30,y=110,width=250)
                self.combo_security_q.current(0)

                #right row 
                security_a=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_a.place(x=30,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=30,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=30,y=220)
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=30,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=120,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x650+0+0")

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

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=20,y=80,width=250)
       
        #right row 1
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=350,y=50)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=350,y=80,width=250)

        #left row 2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=20,y=115)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=20,y=145,width=250)
        
        #right row 2
        email=Label(frame,text="E-mail/Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=350,y=115)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
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

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=350,y=205,width=250)

        #left row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=20,y=240)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=20,y=265,width=250)

        #right row 4
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=350,y=240)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
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
                messagebox.showerror("Error","User Already Exist's, Please Try Another E-Mail",parent=self.root)
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
            self.register_data.destroy()
    
    def return_login(self):
        self.root.destroy()

#main program
if __name__ == "__main__":
    main()