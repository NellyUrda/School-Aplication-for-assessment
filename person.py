class Person:
    name = None
    __email = None
    __password = None

    def __init__(self, name, email, password):
        self.name = name
        self.__email = email
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


class Teacher(Person):
    discipline = None

    def __init__(self, name, email, password, discipline):
        super().__init__(name, email, password)
        self.discipline = discipline


class Student(Person):
    __points = 0

    def __init__(self, name, email, password, points):
        super().__init__(name, email, password)
        self.__points = points

    def set_points(self, points):
        self.__points = points

    def get_points(self):
        return self.__points
