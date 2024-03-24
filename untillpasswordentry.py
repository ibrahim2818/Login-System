from tkinter import *

from PIL import ImageTk  # for adding jpg images

#functionality part
def user_enter(meow):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)  # remove username jokhon cursol nibe

def password_enter(meow):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,END)



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


usernameEntry= Entry(login_window, width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', user_enter)  #username lekha remove er jonno
frame1= Frame(login_window, width=250,height=2,bg='firebrick1')
frame1.place(x=580, y=222)




passwordEntry= Entry(login_window, width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=250)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', password_enter) #password lekha remove er jonno
Frame(login_window, width=250,height=2,bg='firebrick1').place(x=580, y=272)




login_window.mainloop() # helps to view windows
