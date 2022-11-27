import os.path
import shutil
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import glob
import os


# Teachers page
# includes the disciplines that teachers teach
class TeacherDisciplines:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("Teacher/Disciplines")
        master.config(bg="gray")

        title_label = Label(master, text=" *Choose a discipline", font=("Ariel", 12),
                            bg="gray")
        title_label.place(x=10, y=40, width=200, height=25)

        math_button = Button(master, text="Mathematics", font=("Ariel", 14, "bold"),
                             command=self.open_math_tests)
        math_button.place(x=20, y=70, width=200, height=30)

        geography_button = Button(master, text="Geography", font=("Ariel", 14, "bold"),
                                  command=self.open_geography_tests)
        geography_button.place(x=20, y=120, width=200, height=30)

    # Mathematics Button
    # opens the page for Math Discipline
    def open_math_tests(self):
        window = Tk()
        teachers_tests = TeachersMathDiscipline(window)

    # Geography Button
    # opens the page for Geography Discipline
    def open_geography_tests(self):
        window = Tk()
        teachers_tests = TeachersGeographyDiscipline(window)


# Math discipline Page
# teachers can see all the tests, they can add new tests
# after a new test is added, it will appear in both folders( teachers and students )
class TeachersMathDiscipline:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.config(bg="gray")
        master.title("Teacher/Disciplines/Math")

        self.tests_label = Label(master, text="Tests", font=("Ariel", 14), bg="gray")
        self.tests_label.place(x=9, y=5, width=100, height=25)

        my_frame = Frame(master)
        my_frame.place(x=20, y=30, width=270, height=560)
        # add scroll bar to frame
        my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

        self.files_listbox = Listbox(my_frame, font=("Ariel", 14), yscrollcommand=my_scrollbar.set)
        self.files_listbox.place(x=0, y=0, width=250, height=560)
        # get all files paths
        all_files = glob.glob("C:\\Users\\urdan\\OneDrive\\Desktop\\Math tests\\*.txt")
        for i in range(len(all_files)):
            # add each file to list box (only the name, not all path)
            self.files_listbox.insert(i, all_files[i][32:])
        self.files_listbox.bind("<<ListboxSelect>>", self.open_test)
        # configure scrollbar
        my_scrollbar.config(command=self.files_listbox.yview)  # scroll to my listbox
        my_scrollbar.pack(side=RIGHT, fill=Y)

        self.test_label = Label(master, text="", font=("Ariel", 14))
        self.test_label.place(x=300, y=30, width=490, height=560)

        self.add_button = Button(master, text="Add++", bg="green", font=("Ariel", 12),
                                 command=self.add_new_test)
        self.add_button.place(x=715, y=5, width=70, height=25)

    # after we select a test from the listbox, il will be open in the next text widget
    def open_test(self, event):
        # list of all files path
        all_files = glob.glob("C:\\Users\\urdan\\OneDrive\\Desktop\\Math tests\\*.txt")
        for i in range(len(all_files)):
            for index in self.files_listbox.curselection():
                # if the name of the file(not all path) is equal to the listbox item selected
                # open the file and put the text in the textWidget
                if all_files[i][32:] == self.files_listbox.get(index):
                    with open(all_files[i], "r") as math_file:
                        math_test = math_file.read()
                        self.test_label.config(text=math_test)

    # Add++ button
    # opens the window were the teacher adds a new test
    def add_new_test(self):
        self.master.destroy()
        window = Tk()
        add_test = AddMathTest(window)


# Add new test Page
# the teacher adds new test . It will be saved in both folders (teachers, students)
class AddMathTest:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.config(bg="gray")
        master.title("Math/Add new test")

        self.new_test_text = Text(master, font=("Ariel", 14))
        self.new_test_text.place(x=10, y=10, width=760, height=560)

        self.add_button = Button(master, text="Add test", bg="green", font=("Ariel", 12),
                                 command=self.add_test)
        self.add_button.place(x=50, y=570, width=100, height=25)

    def add_test(self):
        # write and save the test from text widget into a file
        try:
            path = filedialog.asksaveasfilename(initialdir="C:\\Users\\urdan\\OneDrive\\Desktop\\Math tests\\",
                                                title="Open text File",
                                                filetypes=[("Text File", ".txt"), ("All files", ".*")],
                                                defaultextension=".txt")
            with open(path, 'w') as new_test_file:
                new_test_file.write(self.new_test_text.get(1.0, END))
        except FileNotFoundError:
            tkinter.messagebox.showinfo(message=" File not found !")

        # get all math files paths
        all_math_files = glob.glob("C:\\Users\\urdan\\OneDrive\\Desktop\\Math tests\\*.txt")

        # get the latest file added in folder
        latest_file_path = max(all_math_files, key=os.path.getctime)

        # copy the latest file added into the students folder
        shutil.copy2(latest_file_path, "C:\\Users\\urdan\\OneDrive\\Desktop\\Student-math tests\\")

        self.my_text.delete(1.0, END)


# Geography discipline Page
# teachers can see all the tests, they can add new tests
# after a new test is added, it will appear in both folders( teachers and students )
class TeachersGeographyDiscipline:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.config(bg="gray")
        master.title("Teacher/Disciplines/Geography")

        self.tests_label = Label(master, text="Tests", font=("Ariel", 14), bg="gray")
        self.tests_label.place(x=9, y=5, width=100, height=25)

        my_frame = Frame(master)
        my_frame.place(x=20, y=30, width=270, height=560)
        # add scroll bar to frame
        my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

        self.files_listbox = Listbox(my_frame, font=("Ariel", 14), yscrollcommand=my_scrollbar.set)
        self.files_listbox.place(x=0, y=0, width=250, height=560)
        # get all files paths
        all_files = glob.glob("C:\\Users\\urdan\\OneDrive\\Desktop\\Geography tests\\*.txt")
        for i in range(len(all_files)):
            # add each file to list box (only the name, not all path)
            self.files_listbox.insert(i, all_files[i][32:])
        self.files_listbox.bind("<<ListboxSelect>>", self.open_test)
        # configure scrollbar
        my_scrollbar.config(command=self.files_listbox.yview)  # scroll to my listbox
        my_scrollbar.pack(side=RIGHT, fill=Y)

        self.test_label = Label(master, text="", font=("Ariel", 14))
        self.test_label.place(x=300, y=30, width=490, height=560)

        self.add_button = Button(master, text="Add++", bg="green", font=("Ariel", 12),
                                 command=self.add_new_test)
        self.add_button.place(x=715, y=5, width=70, height=25)

    # after we select a test from the listbox, il will be open in the next text widget
    def open_test(self, event):
        # list of all files path
        all_files = glob.glob("C:\\Users\\urdan\\OneDrive\\Desktop\\Geography tests\\*.txt")
        for i in range(len(all_files)):
            for index in self.files_listbox.curselection():
                # if the name of the file(not all path) is equal to the listbox item selected
                # open the file and put the text in the textWidget
                if all_files[i][32:] == self.files_listbox.get(index):
                    with open(all_files[i], "r") as math_file:
                        math_test = math_file.read()
                        self.test_label.config(text=math_test)

    # Add++ button
    # opens the window were  the teacher adds a new test
    def add_new_test(self):
        self.master.destroy()
        window = Tk()
        add_test = AddNewTest(window)


# Add new test Page
# the teacher adds new test . It will be saved in both folders (teachers, students)
class AddNewTest:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.config(bg="gray")
        master.title("Geography/Add new test")

        self.new_test_text = Text(master, font=("Ariel", 14))
        self.new_test_text.place(x=10, y=10, width=760, height=560)

        self.add_button = Button(master, text="Add test", bg="green", font=("Ariel", 12),
                                 command=self.add_test)
        self.add_button.place(x=50, y=570, width=100, height=25)

    def add_test(self):
        # write and save the test from text widget into a file
        try:
            path = filedialog.asksaveasfilename(initialdir="C:\\Users\\urdan\\OneDrive\\Desktop\\Geography tests\\",
                                                title="Open text File",
                                                filetypes=[("Text File", ".txt"), ("All files", ".*")],
                                                defaultextension=".txt")
            with open(path, 'w') as new_test_file:
                new_test_file.write(self.new_test_text.get(1.0, END))
        except FileNotFoundError:
            tkinter.messagebox.showinfo(message=" File not found !")

        # get all math files paths
        all_math_files = glob.glob("C:/Users/urdan/OneDrive/Desktop/Geography tests/*.txt")

        # get the latest file added in folder
        latest_file_path = max(all_math_files, key=os.path.getctime)

        # copy the latest file added into the students folder
        shutil.copy2(latest_file_path, "C:\\Users\\urdan\\OneDrive\\Desktop\\Student-geography tests\\")

        self.my_text.delete(1.0, END)
