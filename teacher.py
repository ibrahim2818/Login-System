from tkinter import *
teacher_window= Tk()


teacher_window.resizable(0,0)
teacher_window.geometry('1274x717+50+50')
teacher_window.title('Teacher Window')
background= PhotoImage(file= 'bgs.png')
backgroundLabel=Label(teacher_window, image= background)
backgroundLabel.place(x=0, y=0)

def to_user():
    teacher_window.destroy()
    import signin

welcomeLabel= Label(teacher_window, text='''Teacher's Dashboard''',font=('open Sans', 25, 'bold'),
                fg='firebrick1',bg='white',bd=10).place(x=30, y=30)

courseImage = PhotoImage(file= 'teachercourse.png')
courseButton= Button(teacher_window, image= courseImage,bd=5,bg='black').place(x=550, y=200)
regLabel= Label(teacher_window, text= 'My Courses',font=('open Sans', 20, 'bold'),
                fg='firebrick1',bg='white',bd=10). place(x=580, y=450)

# examImage = PhotoImage(file= 'exam.png')
# examButton= Button(teacher_window, image= examImage,bd=5,bg='black').place(x=850, y=200)
# examLabel= Label(teacher_window, text= 'Exam',font=('open Sans', 20, 'bold'),
#                 fg='firebrick1',bg='white',bd=10). place(x=880, y=450)


# admitImage = PhotoImage(file= 'admit.png')
# admitButton= Button(teacher_window, image= admitImage,bd=5,bg='black').place(x=250, y=200)
# admitLabel= Label(teacher_window, text= 'Admit card',font=('open Sans', 20, 'bold'),
#                 fg='firebrick1',bg='white',bd=10). place(x=285, y=450)


backButton= Button(teacher_window,text='< Back',font=('open Sans', 20, 'bold'),fg='firebrick1',bg='white',
                   bd=10,command= to_user). place(x=1100, y=640)
teacher_window.mainloop()