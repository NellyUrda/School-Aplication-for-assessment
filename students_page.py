import tkinter.messagebox
from tkinter import *
from tkinter import filedialog


# students page
# includes all the courses that students take
class StudentCourses:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("Student/Courses")
        master.config(bg="gray")

        title_label = Label(master, text=" *Choose the course", font=("Ariel", 12),
                            bg="gray")
        title_label.place(x=10, y=40, width=200, height=25)

        math_button = Button(master, text="Mathematics", font=("Ariel", 14, "bold"),
                             command=self.math_course)
        math_button.place(x=20, y=70, width=200, height=30)

        geography_button = Button(master, text="Geography", font=("Ariel", 14, "bold"),
                                  command=self.geography_course)
        geography_button.place(x=20, y=120, width=200, height=30)

    # Mathematics Button
    # opens the page for Mathematics course
    def math_course(self):
        window = Tk()
        student_tests = StudentMathCourse(window)

    # Geography Button
    # opens the page for Geography course
    def geography_course(self):
        window = Tk()
        student_tests = StudentGeographyCourse(window)


# Match course Page
# students can see all the tests, take a test and submit it to the page
class StudentMathCourse:
    def __init__(self, window):
        self.window = window
        window.geometry("900x600")
        window.config(bg="gray")
        window.title("Student/Courses/Math")

        self.label_name = Label(window, text="Mathematics tests ", bg="gray", font=("Ariel", 12))
        self.label_name.place(x=10, y=5, width=150, height=20)

        self.test_label = Label(window, text=" ", font=("Ariel", 14))
        self.test_label.place(x=10, y=30, width=375, height=500)

        self.my_text = Text(window, font=("Ariel", 14))
        self.my_text.place(x=390, y=30, width=475, height=500)

        self.open_test_button = Button(window, text="Tests", bg="green", font=("Ariel", 10, "bold"),
                                       command=self.open_test)
        self.open_test_button.place(x=110, y=550, width=100, height=30)

        self.submit_test_button = Button(window, text="Submit test", bg="green", font=("Ariel", 10, "bold"),
                                         command=self.submit_test)
        self.submit_test_button.place(x=470, y=550, width=100, height=30)

    # Tests button
    # open a test from specific folder
    def open_test(self):
        try:
            path = filedialog.askopenfilename(initialdir="C:\\Users\\urdan\\OneDrive\\Desktop\\Student-math tests\\",
                                              title="Open text File",
                                              defaultextension=".txt")
            with open(path, "r") as math_test_file:
                math_test = math_test_file.read()
                self.test_label.config(text=math_test)
                math_test_file.close()
        except FileNotFoundError:
            tkinter.messagebox.showinfo(message="File not found !")

    # Submit test button
    # after the student take a test, this will be saved in the teachers folder
    def submit_test(self):
        try:
            path = filedialog.asksaveasfilename(initialdir="C:/Users/urdan/OneDrive/Desktop/Math tests",
                                                title="Open text File",
                                                filetypes=[("Text File", ".txt"), ("All files", ".*")],
                                                defaultextension=".txt")
            with open(path, "w") as my_test_file:
                my_test_file.write(self.my_text.get(1.0, END))
                self.my_text.delete(1.0, END)
                my_test_file.close()
        except FileNotFoundError:
            tkinter.messagebox.showinfo(message="File not found !")


# Geography course Page
# students can see all the tests, take a test and submit it into the page
class StudentGeographyCourse:
    def __init__(self, window):
        self.window = window
        window.geometry("1000x600")
        window.config(bg="gray")
        window.title("Student/Courses/Geography")

        self.label_name = Label(window, text="Geography tests ", bg="gray", font=("Ariel", 12))
        self.label_name.place(x=10, y=5, width=150, height=20)

        self.test_label = Label(window, text=" ", font=("Ariel", 12))
        self.test_label.place(x=10, y=30, width=550, height=500)

        self.my_text = Text(window, font=("Ariel", 14))
        self.my_text.place(x=570, y=30, width=375, height=500)

        self.open_test_button = Button(window, text="Tests", bg="green", font=("Ariel", 10, "bold"),
                                       command=self.open_test)
        self.open_test_button.place(x=110, y=550, width=100, height=30)

        self.submit_test_button = Button(window, text="Submit test", bg="green", font=("Ariel", 10, "bold"),
                                         command=self.submit_test)
        self.submit_test_button.place(x=700, y=550, width=100, height=30)

    # Tests button
    # open a test from specific folder
    def open_test(self):
        try:
            path = filedialog.askopenfilename(initialdir="C:/Users/urdan/OneDrive/Desktop/Student-geography tests",
                                              title="Open text File",
                                              defaultextension=".txt")
            with open(path, "r") as geography_test_file:
                geography_test = geography_test_file.read()
                self.test_label.config(text=geography_test)
                geography_test_file.close()
        except FileNotFoundError:
            tkinter.messagebox.showinfo(message="File not found!")

    # Submit test button
    # after the student takes a test, this will be saved in the teachers folder
    def submit_test(self):
        try:
            path = filedialog.asksaveasfilename(initialdir="C:/Users/urdan/OneDrive/Desktop/Geography tests",
                                                title="Open text File",
                                                filetypes=[("Text File", ".txt"), ("All files", ".*")],
                                                defaultextension=".txt")
            with open(path, "w") as my_test_file:
                my_test = my_test_file.write(self.my_text.get(1.0, END))
                self.my_text.delete(1.0, END)
                my_test_file.close()
        except FileNotFoundError:
            tkinter.messagebox.showinfo(message="File not found!")
