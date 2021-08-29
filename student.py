from configparser import ParsingError
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Face Recognition System")

        #variables------------------------------------------------------------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


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
        img3=img3.resize((1400,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=700)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=8,y=40,width=1350,height=550)

        #left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times new roman",11,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=510)

        img_left=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\varenda.png")
        img_left=img_left.resize((640,80),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=640,height=80)

        #(Inside student[LEFT] details frame)
        #Current Course Information Frame
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Course Details",font=("Times new roman",12,"bold"),bg="white")
        current_course_frame.place(x=5,y=80,width=640,height=100)

        #Department Label + ComboBox
        dep_label=Label(current_course_frame,text="Department",bg="white",font=("Times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Times new roman",12),width=17,state="readonly")
        dep_combo["values"]=["Select Department","Computer Applications"]
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Course Label + ComboBox
        course_label=Label(current_course_frame,text="Course",bg="white",font=("Times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Times new roman",12),width=17,state="readonly")
        course_combo["values"]=["Select Course","BCA"]
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Year Label + ComboBox
        year_label=Label(current_course_frame,text="Year",bg="white",font=("Times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Times new roman",12),width=17,state="readonly")
        year_combo["values"]=["Select Year","2020-21"]
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester Label + ComboBox
        semester_label=Label(current_course_frame,text="Semester",bg="white",font=("Times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Times new roman",12),width=17,state="readonly")
        semester_combo["values"]=["Select Semester","I","II","III","IV","V","VI"]
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #(Inside student details frame)
        #Class Student Information Frame
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times new roman",12,"bold"),bg="white")
        class_student_frame.place(x=5,y=180,width=640,height=300)

        #Student Label + Entry field
        studentId_label=Label(class_student_frame,text="ID",bg="white",font=("Times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Times new roman",12))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student Name Label + Entry field
        studentName_label=Label(class_student_frame,text="Name",bg="white",font=("Times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class_div Label + Entry field
        class_div_label=Label(class_student_frame,text="Division",bg="white",font=("Times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Times new roman",12),width=18,state="readonly")
        div_combo["values"]=["Select","A"]
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll_no Name Label + Entry field
        roll_no_label=Label(class_student_frame,text="USN No.",bg="white",font=("Times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Times new roman",12))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender Label + Entry field
        gender_label=Label(class_student_frame,text="Gender",bg="white",font=("Times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Times new roman",12),width=18,state="readonly")
        gender_combo["values"]=["Select","Male","Female","Other"]
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB Name Label + Entry field
        dob_label=Label(class_student_frame,text="D.O.B",bg="white",font=("Times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Times new roman",12))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email Label + Entry field
        email_label=Label(class_student_frame,text="Email",bg="white",font=("Times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Times new roman",12))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number Label + Entry field
        phone_label=Label(class_student_frame,text="Phone No.",bg="white",font=("Times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Times new roman",12))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address Label + Entry field
        address_label=Label(class_student_frame,text="City",bg="white",font=("Times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Times new roman",12))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Label + Entry field
        teacher_label=Label(class_student_frame,text="Teacher",bg="white",font=("Times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Times new roman",12))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value='Yes')
        radiobtn1.grid(row=5,column=0,padx=5,pady=5)

        #self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value='No')
        radiobtn2.grid(row=5,column=1,padx=5,pady=5)

        #Buttons Frame 1
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=625,height=35)

        #save Button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0,padx=5,pady=5)
        #update Button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1,padx=5,pady=5)
        #delete Button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        delete_btn.grid(row=0,column=2,padx=5,pady=5)
        #reset Button
        reset_btn=Button(btn_frame,text="Reset",width=19,command=self.reset_data,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3,padx=5,pady=5)

        #Buttons Frame 2
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=235,width=625,height=35)
        #Take Photo Sample Button
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=41,command=self.generate_dataset,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        take_photo_btn.grid(row=0,column=0,padx=5,pady=5)
        #Update Photo Sample Button
        update_photo_btn=Button(btn_frame1,text="Update Photot Sample",width=41,command=self.generate_dataset,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        update_photo_btn.grid(row=0,column=1,padx=5,pady=5)


        #Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times new roman",11,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=510)

        img_right=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\college.png")
        img_right=img_right.resize((640,80),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=640,height=80)

        #search Frame
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("Times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=80,width=640,height=65)

        search_label=Label(search_frame,text="Search By : ",bg="lightblue",font=("Times new roman",10,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("Times new roman",10),width=15,state="readonly")
        search_combo["values"]=["Select","ID/USN","Roll No","Phone No"]
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("Times new roman",10))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Search Button
        search_btn=Button(search_frame,text="Search",width=15,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        search_btn.grid(row=0,column=3,padx=5,pady=5)
        #Show all Button
        showAll_photo_btn=Button(search_frame,text="Show All",width=15,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        showAll_photo_btn.grid(row=0,column=4,padx=5,pady=5)
        
        #Table Frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=150,width=640,height=340)

        #scrollbars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","usn","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #table contents
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("usn",text="USN No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo-Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=150)
        self.student_table.column("course",width=50)
        self.student_table.column("year",width=50)
        self.student_table.column("sem",width=70)
        self.student_table.column("id",width=50)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=50)
        self.student_table.column("usn",width=150)
        self.student_table.column("gender",width=50)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #functions declaration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Fill in all the fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),                                                                                       
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #fetch data function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Fill in all the fields",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update?","Do you want to update this student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,student_id=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                        self.var_gender.get(),                                                                                       
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required to deete data.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student Data???","Do you want to delete this student data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id =%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete Student Data???","Student details has been deleted succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select"),
        self.var_roll.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

        #Generate data set and taking PHOTO SAMPLE
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Fill in all the fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="password",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,student_id=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                        self.var_gender.get(),                                                                                       
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                #---------------Loading Frontal face data from OpenCV------------------------------
                face_classifier=cv2.CascadeClassifier(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Face\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3 , minimum neightbor=5 so 1.3 and 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Face\data\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()