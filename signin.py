from tkinter import *
from tkinter import messagebox

from PIL import ImageTk  # for adding jpg images
import pymysql

#functionality part
def user_enter(meow):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)  # remove username jokhon cursol nibe

def password_enter(meow):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,END)

def hide():
    global closedeye
    closedeye = PhotoImage(file='closeye.png')
    eyeButton.config(image=closedeye, command=show)
    passwordEntry.config(show='*')

def show():
    global openeye
    openeye = PhotoImage(file='openeye.png')
    eyeButton.config(image=openeye, command=hide)
    passwordEntry.config(show='')

def signup_page():
    login_window.destroy()
    import signup
    
def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('error', 'Please enter all required fields')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='2101030')
            mycursor=con.cursor()
        except:
            messagebox.showerror('error', 'connection error')
        query= 'use userdata'
        mycursor.execute(query)
        query='SELECT *from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', "Login successful")

def forget_data():
    login_window.destroy()
    import otp




login_window=Tk() #creating object of Tkinter class
login_window.geometry('990x660+50+50')  # for window size # for using "place"
login_window.resizable(0,0) #jate window size thik thake size boro kora jabena 
login_window.title('LOGIN PAGE') #title change er jonno

bgImage= ImageTk.PhotoImage(file='bg.jpg')
bgLabel= Label(login_window,image=bgImage)

bgLabel.place(x=0,y=0)
#alternates of place egula dile geometry use kora lagena
#bgLabel.grid(row=0, column= 0)   # here we can also take place instead of grid but place doesn't increase the window automatically (place(x=0,y=0))
#bgLabel.pack()   # edike pack r grid same but pack e value na dile starting point theke suru hoy



heading= Label(login_window, text="USER LOGIN", font=("Microsoft Yahei UI Light",23,"bold"),bg='white',fg='firebrick1') 
#for adding user login,fg= fonts color & bg = font background color
heading.place(x=605, y=110)


#user entry
usernameEntry= Entry(login_window, width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', user_enter)  #username lekha remove er jonno
frame1= Frame(login_window, width=250,height=2,bg='firebrick1')
frame1.place(x=580, y=222)



#password entry
passwordEntry= Entry(login_window, width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=250)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', password_enter) #password lekha remove er jonno
Frame(login_window, width=250,height=2,bg='firebrick1').place(x=580, y=272)




#eye Button
openeye= PhotoImage(file='openeye.png')
eyeButton= Button(login_window, image=openeye, bd=0, bg='white',activebackground= 'white',cursor='hand2', command= hide)
eyeButton.place(x=800,y=243)



#forget password
forgetButton= Button(login_window, text='Forget Password?',bd=0, bg='white',activebackground='white',
                     cursor='hand2',font=("Microsoft Yahei UI Light",10,"bold"),fg='firebrick1', 
                     activeforeground='firebrick1',command= forget_data)
forgetButton.place(x=720,y=280)



loginButton= Button(login_window,text='Login',font= ('open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1', 
                    activeforeground='white', cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)


orLabel= Label(login_window,text='---------------OR----------------',font=('open Sans',16,'bold'),fg='firebrick1',bg='white')
orLabel.place(x=578,y=400)


#img fb ggl
facebook_logo=PhotoImage(file='facebook.png')
fbLabel= Label(login_window,image=facebook_logo, bg='white').place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel= Label(login_window,image=google_logo, bg='white').place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel= Label(login_window,image=twitter_logo, bg='white').place(x=740,y=440)



accLabel= Label(login_window,text='''Don't have an account?''',font=('open Sans',9,'bold'),fg='firebrick1',bg='white')
accLabel.place(x=578,y=490)

createNewButton= Button(login_window, text='create new one',font=('Open Sans',9, 'bold underline'),
                        fg= 'blue',bg='white', activebackground= 'white', activeforeground='blue',cursor='hand2',bd=0,command= signup_page)
createNewButton.place(x=720,y=490)



login_window.mainloop() # helps to view windows
