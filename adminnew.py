from tkinter import *
import pymysql
from tkinter import messagebox

admin_window = Tk()
admin_window.resizable(0, 0)
admin_window.geometry('1274x717+50+50')
admin_window.title('Admin Window')

# Load the background image
background = PhotoImage(file='bgs.png')
backgroundLabel = Label(admin_window, image=background)
backgroundLabel.place(x=0, y=0)

def user_enter(meow):
    if emailEntry.get()=="Email":
        emailEntry.delete(0,END)

def destroy_all():                      #clearing window 
    welcomeLabel.destroy()             
    addstudentButton.destroy()
    addstudentLabel.destroy()
    addTeacherButton.destroy()
    addTeacherLabel.destroy()
    addadminButton.destroy()
    addadminLabel.destroy()
    backButton.destroy()
    

def add_admin():
    destroy_all()
    try:
            con=pymysql.connect(host='localhost',user='root',password='2101030')
            mycursor=con.cursor()
    except:
            messagebox.showerror('Error','Database connection error')
    try:
        query= 'use userdata'
        mycursor.execute(query)
        query= "select username from data where request IS NULL"
        mycursor.execute(query)



def add_student():
    destroy_all()
    enterButton= Button(admin_window, text= 'Enter',font=('open sans', 18,'bold' ), bg= 'white', fg= 'firebrick1',width=10,
                      activeforeground= 'firebrick1', activebackground= 'white',bd=0 , cursor= 'hand2',command= studentOne)

    emailEntry.place(x=450,y=250)
    enterButton.place(x=570,y=300)
    backButton = Button(admin_window, text='< Back', font=('Open Sans', 20, 'bold'), fg='firebrick1',
                    bg='white', bd=10,command= to_admin)
    backButton.place(x=1100, y=640)

def add_teacher():
    destroy_all()
    enterButton= Button(admin_window, text= 'Enter',font=('open sans', 18,'bold' ), bg= 'white', fg= 'firebrick1',width=10,
                      activeforeground= 'firebrick1', activebackground= 'white',bd=0 , cursor= 'hand2',command= teacherOne)

    emailEntry.place(x=450,y=250)
    enterButton.place(x=570,y=300)
    backButton = Button(admin_window, text='< Back', font=('Open Sans', 20, 'bold'), fg='firebrick1',
                    bg='white', bd=10,command= to_admin)
    backButton.place(x=1100, y=640)


    

emailEntry= Entry(admin_window, width=25,font=("Microsoft Yahei UI Light",20,"bold"),bd=0,fg='firebrick1')

emailEntry.insert(0,'Email')
emailEntry.bind('<FocusIn>', user_enter) 


def adminOne():    #add admin button er command
    

        try:
            con=pymysql.connect(host='localhost',user='root',password='2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connection error')
        try:
            query= 'use userdata'
            mycursor.execute(query)
            query= 'select * from data where email=%s'
            mycursor.execute(query,(emailEntry.get()))
            row1= mycursor.fetchone()
            if row1 is None:
                messagebox.showerror('Email does not exist')
            else:
                query='''update data set role= 'admin' where email=%s'''
                mycursor.execute(query,(emailEntry.get()))
                con.commit()
                messagebox.showinfo('Role Updated Successfully')

        except:
            messagebox.showerror('Error',"Connection error")



def studentOne():   
    if emailEntry.get()=='':
        messagebox.showerror('Error','Enter email')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connection error')
        try:
            query= 'use userdata'
            mycursor.execute(query)
            query= 'select * from data where email=%s'
            mycursor.execute(query,(emailEntry.get()))
            row1= mycursor.fetchone()
            if row1 is None:
                messagebox.showerror('Email does not exist')
            else:
                query='''update data set role= 'student' where email=%s'''
                mycursor.execute(query,(emailEntry.get()))
                con.commit()
                messagebox.showinfo('info','Role Updated Successfully')

        except:
            messagebox.showerror('Error',"Connection error")



def teacherOne():
    if emailEntry.get()=='':
        messagebox.showerror('Error','Enter email')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connection error')
        try:
            query= 'use userdata'
            mycursor.execute(query)
            query= 'select * from data where email=%s'
            mycursor.execute(query,(emailEntry.get()))
            row1= mycursor.fetchone()
            if row1 is None:
                messagebox.showerror('Email does not exist')
            else:
                query='''update data set role= 'teacher' where email=%s'''
                mycursor.execute(query,(emailEntry.get()))
                con.commit()
                messagebox.showinfo('info','Role Updated Successfully')

        except:
            messagebox.showerror('Error',"Connection error")
    

def to_user():
    admin_window.destroy()
    import signin
def to_admin():
    admin_window.destroy()
    import admin



# Create the welcome label
welcomeLabel = Label(admin_window, text="Admin's Dashboard", font=('Open Sans', 25, 'bold'),
                     fg='firebrick1', bg='white', bd=10)
welcomeLabel.place(x=30, y=30)



# Create buttons and labels for adding student, teacher, and admin
studentImage = PhotoImage(file='addstudent.png')
addstudentButton = Button(admin_window, image=studentImage, bd=5, bg='black', command=add_student)
addstudentButton.place(x=850, y=200)
addstudentLabel = Label(admin_window, text='Add as a Student', font=('Open Sans', 20, 'bold'),
                        fg='firebrick1', bg='white', bd=10)
addstudentLabel.place(x=847, y=450)


teacherImage = PhotoImage(file='addteacher.png')
addTeacherButton = Button(admin_window, image=teacherImage, bd=5, bg='black', command= add_teacher)
addTeacherButton.place(x=550, y=200)
addTeacherLabel = Label(admin_window, text='Add as a Teacher', font=('Open Sans', 20, 'bold'),
                        fg='firebrick1', bg='white', bd=10)
addTeacherLabel.place(x=543, y=450)


adminImage = PhotoImage(file='addadmin.png')
addadminButton = Button(admin_window, image=adminImage, bd=5, bg='black',command= add_admin)
addadminButton.place(x=250, y=200)
addadminLabel = Label(admin_window, text='Add as an Admin', font=('Open Sans', 20, 'bold'),
                      fg='firebrick1', bg='white', bd=10)
addadminLabel.place(x=252, y=450)





# Create a back button
backButton = Button(admin_window, text='< Back', font=('Open Sans', 20, 'bold'), fg='firebrick1',
                    bg='white', bd=10,command= to_user)
backButton.place(x=1100, y=640)

admin_window.mainloop()
