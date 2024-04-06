from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox
import smtplib
import random


def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmPasswordEntry.delete(0,END)

def connect_database():
    if emailEntry.get()=='' or userEntry.get()=='' or passwordEntry.get()=='' or confirmPasswordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif passwordEntry.get()!=confirmPasswordEntry.get():
        messagebox.showerror('Error','password Mismatched')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root', password='2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity Issue ,please try again')
        try:
            query= 'create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(50), password varchar(20) )'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        
        query= 'select * from data where username=%s'
        mycursor.execute(query,(userEntry.get()))
        row= mycursor.fetchone()
        query= 'select * from data where email=%s'
        mycursor.execute(query,(emailEntry.get()))
        row1= mycursor.fetchone()
        if row is not None or row1 is not None:
            messagebox.showerror('Error','Username or email already exists')
            
        else:
            global OTP
            global email1,user1,password1
            password = 'nwog fzkf yrrh fxsx'
            my_email= 'janinak2018@gmail.com'
            connection= smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=my_email, password= password)
            connection.sendmail(from_addr=my_email, to_addrs=emailEntry.get(), msg=f"your otp- {OTP}")
            email1= emailEntry.get()
            user1= userEntry.get()
            password1= passwordEntry.get()
            frame.destroy()


            
            otpLabel.place(x=580, y=240)
           
            otpEntry.place(x=580,y=260)
            
            varifyButton.place(x=580,y=300)
email1=None
user1=None
password1= None


def varify_otp():
    global mycursor, con
    global user1, email1, password1

    entered_otp = otpEntry.get()
    try:
        con = pymysql.connect(host='localhost', user='root', password='2101030', database='userdata')
        mycursor = con.cursor()
    except pymysql.err.OperationalError as e:
        messagebox.showerror('Error', f'Database connectivity issue: {str(e)}')
        return

    if entered_otp.isdigit() and int(entered_otp) == OTP:
        messagebox.showinfo('Verification', 'ID Verified')
        try:
            query = 'INSERT INTO data(email, username, password) VALUES (%s, %s, %s)'
            mycursor.execute(query, (email1, user1, password1))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            
            check.set(0)
            signup_window.destroy()
            import signin
        except pymysql.err.ProgrammingError as e:
            messagebox.showerror('Database Error', f'Database error occurred: {str(e)}')
    else:
        messagebox.showerror('Verification', 'Invalid OTP')


def login_page():
    signup_window.destroy()
    import signin
    
OTP= random.randint(1000,10000)


#for window

signup_window=Tk()                           

signup_window.geometry('990x660+50+50') 
signup_window.resizable(0,0) 
signup_window.title('Signup Page')  

background=ImageTk.PhotoImage(file='bg.jpg')
backgroundLabel=Label(signup_window, image= background)
backgroundLabel.place(x=0, y=0)




frame=Frame(signup_window,bg='white') #making frame
frame.place(x=554, y=100)

heading=Label(frame, text= 'CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light', 18, 'bold'), fg='firebrick1',bg='white')
heading.grid(row=0, column=0,padx=10, pady=10)


#email entry
emailLabel=Label(frame, text='Email',font=('Microsoft Yahei UI Light', 10, 'bold'), fg='firebrick1',bg='white')
emailLabel.grid(row=1,column=0, sticky='W',padx=25,pady=(10,0))  #sticky frame er left e neyar jonno use hoise
#pady tuple e rakha hoise ekhane top spacing 10 r bottom 0 rakha hoise



emailEntry= Entry(frame,width=30 ,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
emailEntry.grid(row=3,column=0, sticky='W',padx=25) 

#user entry
userLabel=Label(frame, text='Username',font=('Microsoft Yahei UI Light', 10, 'bold'), fg='firebrick1',bg='white')
userLabel.grid(row=4,column=0, sticky='W',padx=25,pady=(10,0))  

userEntry= Entry(frame,width=30 ,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
userEntry.grid(row=5,column=0, sticky='W',padx=25) 

#password entry
passwordLabel=Label(frame, text='Password',font=('Microsoft Yahei UI Light', 10, 'bold'), fg='firebrick1',bg='white')
passwordLabel.grid(row=6,column=0, sticky='W',padx=25,pady=(10,0))  

passwordEntry= Entry(frame,width=30 ,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
passwordEntry.grid(row=7,column=0, sticky='W',padx=25)


#confirmpassword entry
confirmPasswordLabel=Label(frame, text='Confirm Password',font=('Microsoft Yahei UI Light', 10, 'bold'), fg='firebrick1',bg='white')
confirmPasswordLabel.grid(row=8,column=0, sticky='W',padx=25,pady=(10,0))  

confirmPasswordEntry= Entry(frame,width=30 ,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
confirmPasswordEntry.grid(row=9,column=0, sticky='W',padx=25)

check= IntVar()
termsCondition=Checkbutton(frame, text="I agree to the terms and conditions",font=('open Sans', 9, 'bold'), bg='white',
                           activebackground= 'white',fg='firebrick1' ,activeforeground='firebrick1',cursor='hand2', variable= check)
termsCondition.grid(row=10,column=0, sticky='w', pady=10,padx=15)



signupButton=Button(frame, text="Signup",font=('open Sans', 15, 'bold'), 
                    bg= 'firebrick1',fg='white', width=19 ,activebackground='firebrick1',activeforeground='white', command= connect_database)
signupButton.grid(row=11,column=0,pady=10)



#otp button
otpLabel= Label(signup_window, text= 'OTP',font=('open sans',10,'bold' ), 
                            bg='white', bd=0,fg= 'firebrick1')
otpEntry= Entry(signup_window, text= 'OTP',font=('open sans',13,'bold' ), 
                            fg='white',bg= 'firebrick1',width=25)
varifyButton= Button(signup_window, text= 'Varify',font=('open sans', 16,'bold' ), 
                                 fg= 'white', bg= 'firebrick1',width=19,command=varify_otp,
                                activebackground= 'firebrick1', activeforeground= 'white',bd=0)



haveAccountButton=Button(frame, text="Don't have an account?", font=('open Sans', 9, 'bold'),fg='firebrick1', bg='white',bd=0)
haveAccountButton.grid(row=12, column=0,sticky='W', pady=5, padx=15)

loginButton=Button(frame, text="Login", font=('open Sans', 9, 'bold underline'),fg='blue',bg='white',bd=0, activebackground='white', 
                   activeforeground='blue',command= login_page)
loginButton.place(x=160, y=401)

signup_window.mainloop()
