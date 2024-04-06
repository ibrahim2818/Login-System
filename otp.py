from tkinter import *
sendOtp_window= Tk()
import smtplib
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import random

def sending_otp():
    global store_mail
    if emailEntry =='':
        messagebox.showerror('Error','Enter Email')
    else:
        try:
            con= pymysql.Connection(host='localhost', user= 'root', password= '2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection Error')
        
        query = 'use userdata'
        mycursor.execute(query)
        query = 'SELECT * FROM data WHERE email= %s'
        mycursor.execute(query,(emailEntry.get()))
        row= mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error','Email does not exist')
        else:
            password = 'nwog fzkf yrrh fxsx'
            my_email= 'janinak2018@gmail.com'
            connection= smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=my_email, password= password)
            connection.sendmail(from_addr=my_email, to_addrs=emailEntry.get(), msg=f"your otp- {OTP}")
            store_mail= emailEntry.get()
            emailLabel.destroy()
            emailEntry.destroy()
            otpLabel.place(x=466, y=210)
            otpEntry.place(x=463,y=230)
            varifyButton.place(x=550,y=270)
            

store_mail= None
  
        
        
def varify():
    global store_mail
    entered_otp = otpEntry.get()
    if entered_otp.isdigit() and int(entered_otp) == OTP:
        messagebox.showinfo('Verification', 'ID Verified')
        try:
            con= pymysql.Connection(host='localhost', user= 'root', password= '2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection Error')
        
        query = 'use userdata'
        mycursor.execute(query)
        query ='select username, password from data where email=%s'
        mycursor.execute(query,(store_mail))
        user_data = mycursor.fetchone()
        if user_data:
            username, password = user_data
            messagebox.showinfo('User Data', f'Username: {username}\nPassword: {password}')
            sendOtp_window.destroy()
            import signin
        else:
            messagebox.showerror('Error', 'No user data found for this email')
    else:
        messagebox.showerror('Verification', 'Invalid OTP')
    

        

OTP= random.randint(1000, 10000)   

sendOtp_window.geometry('790x560+50+50')
sendOtp_window.resizable(0,0)
sendOtp_window.title('Sending OTP page')

background=ImageTk.PhotoImage(file='background.jpg')
backgroundLabel=Label(sendOtp_window, image= background)
backgroundLabel.place(x=0, y=0)


emailLabel= Label(sendOtp_window, text= 'Email',font=('open sans',10,'bold' ), bg='white', bd=0,fg= 'firebrick1')
emailLabel.place(x=466, y=210)
emailEntry= Entry(sendOtp_window, text= 'Email',font=('open sans',15,'bold' ), fg='white',bg= 'firebrick1',width=25)
emailEntry.place(x=463,y=230)

sendOtpButton= Button(sendOtp_window, text= 'Send OTP',font=('open sans', 10,'bold' ), fg= 'white', bg= 'firebrick1',width=10,
                      activebackground= 'firebrick1', activeforeground= 'white',bd=0,command=sending_otp)
sendOtpButton.place(x=550,y=270)


otpLabel= Label(sendOtp_window, text= 'OTP',font=('open sans',10,'bold' ), bg='white', bd=0,fg= 'firebrick1')

otpEntry= Entry(sendOtp_window, text= 'OTP',font=('open sans',15,'bold' ), fg='white',bg= 'firebrick1',width=25)


varifyButton= Button(sendOtp_window, text= 'Varify',font=('open sans', 10,'bold' ), fg= 'white', bg= 'firebrick1',width=10,
            activebackground= 'firebrick1', activeforeground= 'white',bd=0, command=varify)





sendOtp_window.mainloop()