import datetime


class Person:
    def __init__(self, name):
        """Assumes name is a string. Create a person."""
        self._name = name
        try:
            last_blank = name.rindex(" ")
            self._last_name = name[last_blank + 1 :]
        except:
            self._last_name = name
        self._birthday = None

    def get_name(self):
        """Returns self's first name"""
        return self._name

    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name

    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self._birthday = birthdate

    def get_age(self):
        """Returns's self's current age in days"""
        if not self._birthday:
            raise ValueError("Birthday not defined.")
        return (datetime.datetime.today() - self._birthday).days

    def __lt__(self, other):
        """Assume other a Person
        Returns True if self precedes other in alphabetical order, False otherwise.
        Comparison is based on last names, if these are same, full names are compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns self's name"""
        return self._name


class MIT_person(Person):

    _next_id_num = 0

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def is_student(self):
        return isinstance(self, Student)

    def __lt__(self, other):
        return self._id_num < other._id_num


class Student(MIT_person):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year

    def get_class(self):
        return self._year


class Grad(Student):
    pass


me = Person("Harry Potter")
him = Person("Barack Hussein Obama")
her = Person("Madonna")
print(him.get_last_name())
him.set_birthday(datetime.datetime(1961, 8, 4))
her.set_birthday(datetime.datetime(1958, 8, 16))
print(him.get_name(), "is", him.get_age(), "days old")

p1 = MIT_person("Barbara Beaver")
print(f"{p1}'s id number is {p1.get_id_num()}")
p2 = MIT_person("Billy Bob Beaver")
p3 = MIT_person("Billy Bob Beaver")
p4 = Person("Billy Bob Beaver")

print(f"p1 < p2 = {p1 < p2}")
print(f"p3 < p2 = {p3 < p2}")
print(f"p4 < p1 = {p4 < p1}")
# print(f"p1 < p4 = {p1 < p4}")

p5 = Grad("Buzz Aldrin")
p6 = UG("Billy Beaver", 1984)
print(f"{p5} is a graduate student is {type(p5) == Grad}")
print(f"{p5} is an undergraduate student is {type(p5) == UG}")

print(f"{p5} is a student is {p5.is_student()}")
print(f"{p6} is a student is {p6.is_student()}")
print(f"{p3} is a student is {p3.is_student()}")
