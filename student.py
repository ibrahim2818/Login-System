from tkinter import *
student_window= Tk()


student_window.resizable(0,0)
student_window.geometry('1274x717+50+50')
student_window.title('Student Window')
background= PhotoImage(file= 'bgs.png')
backgroundLabel=Label(student_window, image= background)
backgroundLabel.place(x=0, y=0)

def to_user():
    student_window.destroy()
    import signin

welcomeLabel= Label(student_window, text='''Student's Dashboard''',font=('open Sans', 25, 'bold'),
                fg='firebrick1',bg='white',bd=10).place(x=30, y=30)


regImage = PhotoImage(file= 'registration.png')
registrationButton= Button(student_window, image= regImage,bd=5,bg='black').place(x=850, y=200)
regLabel= Label(student_window, text= 'Registration',font=('open Sans', 20, 'bold'),
                fg='firebrick1',bg='white',bd=10). place(x=880, y=450)

examImage = PhotoImage(file= 'exam.png')
examButton= Button(student_window, image= examImage,bd=5,bg='black').place(x=550, y=200)
examLabel= Label(student_window, text= 'Exam',font=('open Sans', 20, 'bold'),
                fg='firebrick1',bg='white',bd=10). place(x=620, y=450)


admitImage = PhotoImage(file= 'admit.png')
admitButton= Button(student_window, image= admitImage,bd=5,bg='black').place(x=250, y=200)
admitLabel= Label(student_window, text= 'Admit card',font=('open Sans', 20, 'bold'),
                fg='firebrick1',bg='white',bd=10). place(x=285, y=450)

backButton= Button(student_window,text='< Back',font=('open Sans', 20, 'bold'),fg='firebrick1',bg='white',
                   bd=10,command= to_user). place(x=1100, y=640)





student_window.mainloop()