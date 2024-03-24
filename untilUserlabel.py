from tkinter import *

from PIL import ImageTk  # for adding jpg images

#functionality part
def on_enter(meow):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)  # remove username jokhon cursol nibe



root=Tk() #creating object of Tkinter class
root.geometry('990x660+50+50')  # for window size # for using "place"
root.resizable(0,0) #jate window size thik thake size boro kora jabena 
root.title('LOGIN PAGE') #title change er jonno

bgImage= ImageTk.PhotoImage(file='bg.jpg')
bgLabel= Label(root,image=bgImage)

bgLabel.place(x=0,y=0)
#alternates of place egula dile geometry use kora lagena
#bgLabel.grid(row=0, column= 0)   # here we can also take place instead of grid but place doesn't increase the window automatically (place(x=0,y=0))
#bgLabel.pack()   # edike pack r grid same but pack e value na dile starting point theke suru hoy



heading= Label(root, text="USER LOGIN", font=("Microsoft Yahei UI Light",23,"bold"),bg='white',fg='firebrick1') 
#for adding user login,fg= fonts color & bg = font background color



usernameEntry= Entry(root, width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', on_enter)  #username lekha remove er jonno

heading.place(x=605, y=110)



root.mainloop() # helps to view windows
