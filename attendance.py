from configparser import ParsingError
from tkinter import* 
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os 
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Attendance  System")

        #------------------------Variables----------------------------
        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

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
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=8,y=40,width=1350,height=555)

        #left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times new roman",11,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=515)

        img_left=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\college.png")
        img_left=img_left.resize((640,180),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=640,height=180)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=190,width=640,height=295)

        #------------------------labels and entry fields--------------------
        
        #USN Label + Entry field
        usn_label=Label(left_inside_frame,text="USN/ID",bg="white",font=("Times new roman",12,"bold"))
        usn_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        usn_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_usn,font=("Times new roman",12))
        usn_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Name Label + Entry field
        name_label=Label(left_inside_frame,text="Name",bg="white",font=("Times new roman",12,"bold"))
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("Times new roman",12))
        name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Course Label + Entry field
        course_label=Label(left_inside_frame,text="Course",bg="white",font=("Times new roman",12,"bold"))
        course_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        course_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_course,font=("Times new roman",12))
        course_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Semester Label + Entry field
        semester_label=Label(left_inside_frame,text="Semester",bg="white",font=("Times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        semester_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_sem,font=("Times new roman",12))
        semester_entry.grid(row=1,column=3,padx=10,sticky=W)

        #Time Label + Entry field
        time_label=Label(left_inside_frame,text="Time",bg="white",font=("Times new roman",12,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("Times new roman",12))
        time_entry.grid(row=2,column=1,padx=10,sticky=W)

        #Date Label + Entry field
        date_label=Label(left_inside_frame,text="Date",bg="white",font=("Times new roman",12,"bold"))
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("Times new roman",12))
        date_entry.grid(row=2,column=3,padx=10,sticky=W)

        #Attendance Status Label + Combo box
        status_label=Label(left_inside_frame,text="Attendance Status",bg="white",font=("Times new roman",12,"bold"))
        status_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_status,font=("Times new roman",12),width=18,state="readonly")
        self.status_combo["values"]=["Select","Present","Absent"]
        self.status_combo.current(0)
        self.status_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Buttons Frame 1
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=170,width=625,height=40)

        #Import Button
        import_btn=Button(btn_frame,text="Import",command=self.importCSV,width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        import_btn.grid(row=0,column=0,padx=5,pady=5)
        #Export Button
        export_btn=Button(btn_frame,text="Export",command=self.exportCSV,width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        export_btn.grid(row=0,column=1,padx=5,pady=5)
        #Update Button
        update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=2,padx=5,pady=5)
        #reset Button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",10,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3,padx=5,pady=5)


        #Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("Times new roman",11,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=515)

        img_right=Image.open(r"C:\Users\Kishan Dahiya\AppData\Local\Programs\Python\Python39\Project\Pictures\varenda.png")
        img_right=img_right.resize((640,180),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=640,height=180)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=190,width=640,height=295)

        #Scroll Bars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("usn","name","course","sem","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        #table contents
        self.AttendanceReportTable.heading("usn",text="USN/ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("course",text="Course")
        self.AttendanceReportTable.heading("sem",text="Semester")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("usn",width=50)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("course",width=50)
        self.AttendanceReportTable.column("sem",width=70)
        self.AttendanceReportTable.column("time",width=70)
        self.AttendanceReportTable.column("date",width=70)
        self.AttendanceReportTable.column("attendance",width=70)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        #======================fetching data to table=====================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #Import Data Function
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export Data Function
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found To Export!!!",parent=self.root)
                return False 
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                csvwrite=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Success","Your Data Is Exported to "+os.path.basename(fln)+" Succesfully.")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #Fetch data 
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_usn.set(row[0])
        self.var_name.set(row[1])
        self.var_course.set(row[2])
        self.var_sem.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_status.set(row[6])
    
    #reset function
    def reset_data(self):
        self.var_usn.set(""),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_sem.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_status.set("Select")


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()