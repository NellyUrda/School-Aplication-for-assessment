import tkinter.messagebox
from tkinter import *
from students_page import StudentCourses
from teachers_page import TeacherDisciplines
from person import Teacher, Student

window = Tk()

# the instances of the Student and Teacher classes
# the second and the third argument of each object represent the username(email) and password
# that they use in order to login
student1 = Student("Ionel", "ionel@gmail.com", "1234", 0)
student2 = Student("Alexa", "alexa@gmail.com", "1111", 0)
math_teacher = Teacher("Diana Alexa", "diana@gmail.com", "2345", "math")
geograpy_teacher = Teacher("Alin Ion", "alin@gmail.com", "2222", "geography")
students = [student1, student2]
teachers = [math_teacher, geograpy_teacher]


class Login:
    def __init__(self, master):
        master.geometry("800x600")
        master.title("Login")
        master.config(bg="gray")

        frame = Frame(master)
        frame.place(x=100, y=50, width=500, height=350)

        self.login_lable = Label(frame, text="Login", font=("Ariel", 18))
        self.login_lable.place(x=5, y=10, width=100, height=30)

        self.username_label = Label(frame, text="Username", font=("Ariel", 12, "bold"))
        self.username_label.place(x=5, y=70, width=100, height=30)

        self.username_entry = Entry(frame)
        self.username_entry.place(x=110, y=70, width=200, height=25)

        self.user_label = Label(frame, text="* use your email address", font=("Ariel", 10))
        self.user_label.place(x=90, y=100, width=200, height=25)

        self.password_label = Label(frame, text="Password", font=("Ariel", 12, "bold"))
        self.password_label.place(x=5, y=140, width=100, height=30)

        self.password_entry = Entry(frame, show="*")
        self.password_entry.place(x=110, y=140, width=200, height=25)

        self.identity_label = Label(frame, text="Identity:", font=("Ariel", 12, "bold"))
        self.identity_label.place(x=5, y=190, width=100, height=30)

        self.x = StringVar(value=" ")
        self.t_radio_button = Radiobutton(frame, text="Teacher", variable=self.x, value="t",
                                          font=("Ariel", 12, "bold"))
        self.t_radio_button.place(x=110, y=190, width=100, height=30)

        self.s_radio_button = Radiobutton(frame, text="Student", variable=self.x, value="s",
                                          font=("Ariel", 12, "bold"))
        self.s_radio_button.place(x=200, y=190, width=100, height=30)

        self.login_button = Button(frame, text='Login', font=("Ariel", 12), bg="green",
                                   activebackground="green", command=self.login, )
        self.login_button.place(x=160, y=240, width=100, height=25)

    # Login Button
    # Enter username/password, choose identification (teacher or student) then login
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_found = False
        if self.x.get() == "t":
            for teacher in teachers:
                if (username == teacher.get_email()) and (password == teacher.get_password()):
                    root = Tk()
                    discipline = TeacherDisciplines(root)
                    user_found = True
        elif self.x.get() == "s":
            for student in students:
                if (username == student.get_email()) and (password == student.get_password()):
                    root = Tk()
                    courses = StudentCourses(root)
                    user_found = True

        if not user_found:
            tkinter.messagebox.showinfo(message="Wrong Username or password!")

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.x.set(" ")


login = Login(window)
window.mainloop()
