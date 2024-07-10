from tkinter import *
welcome_window = Tk()
from PIL import ImageTk

def enter_user():
    welcome_window.destroy()
    import signin

welcome_window.geometry('1292x721+50+50')
welcome_window.resizable(0,0)
welcome_window.title('Welcome page')

background = ImageTk.PhotoImage(file='welcomePage1.jpg')
backgroundLabel = Label(welcome_window, image=background)
backgroundLabel.place(x=0, y=0)

welcome = Label(welcome_window, text='Click here to enter...', font=('open sans', 15, 'bold'), bg='white', bd=0, fg='firebrick1')
welcome.place(x=480, y=140)

enterButton = Button(welcome_window, text='Enter', font=('open sans', 18, 'bold'), bg='white', fg='firebrick1', width=10,
                     activeforeground='firebrick1', activebackground='white', bd=0, command=enter_user, cursor='hand2')
enterButton.place(x=570, y=172)

welcome_window.mainloop()
