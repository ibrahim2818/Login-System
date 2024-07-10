from tkinter import *
from tkinter import messagebox
from PIL import ImageTk  # for adding jpg images
import pymysql

# Functionality part
def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)  # Remove "Username" when cursor is placed

def password_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)  # Remove "Password" when cursor is placed

def hide():
    closedeye = PhotoImage(file='closeye.png')
    eyeButton.config(image=closedeye, command=show)
    passwordEntry.config(show='*')

def show():
    openeye = PhotoImage(file='openeye.png')
    eyeButton.config(image=openeye, command=hide)
    passwordEntry.config(show='')

def signup_page():
    login_window.destroy()
    import signup
    
def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Please enter all required fields')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='2101030')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection error')
            return

        query = 'USE userdata'
        mycursor.execute(query)
        query = 'SELECT * FROM data WHERE username=%s AND password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        
        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', "Login successful")
            query = 'SELECT role FROM data WHERE username=%s AND password=%s'
            mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            result = mycursor.fetchone()
            role = result[0]
            
            if role == 'admin':
                login_window.destroy()
                import admin
            elif role == 'student':
                login_window.destroy()
                import student
            elif role == 'teacher':
                login_window.destroy()
                import teacher
            else:
                messagebox.showinfo('Info', 'An admin needs to approve your request')

def forget_data():
    login_window.destroy()
    import otp

# Main GUI setup
login_window = Tk()  # Creating an object of Tkinter class
login_window.geometry('990x660+50+50')  # Setting window size and position
login_window.resizable(0, 0)  # Disabling window resize
login_window.title('LOGIN PAGE')  # Setting window title

bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text="USER LOGIN", font=("Microsoft Yahei UI Light", 23, "bold"), bg='white', fg='firebrick1')
heading.place(x=605, y=110)

# User entry
usernameEntry = Entry(login_window, width=25, font=("Microsoft Yahei UI Light", 11, "bold"), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

# Password entry
passwordEntry = Entry(login_window, width=25, font=("Microsoft Yahei UI Light", 11, "bold"), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=250)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=272)

# Eye Button
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=243)

# Forget password
forgetButton = Button(login_window, text='Forget Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=("Microsoft Yahei UI Light", 10, "bold"), fg='firebrick1', activeforeground='firebrick1', command=forget_data)
forgetButton.place(x=720, y=280)

# Login button
loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', activebackground='firebrick1',
                     activeforeground='white', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='---------------OR----------------', font=('Open Sans', 16, 'bold'), fg='firebrick1', bg='white')
orLabel.place(x=578, y=400)

# Social media icons
facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

# Create account option
accLabel = Label(login_window, text="Don't have an account?", font=('Open Sans', 9, 'bold'), fg='firebrick1', bg='white')
accLabel.place(x=578, y=490)

createNewButton = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'), fg='blue', bg='white',
                         activebackground='white', activeforeground='blue', cursor='hand2', bd=0, command=signup_page)
createNewButton.place(x=720, y=490)

login_window.mainloop()  # Helps to view window
