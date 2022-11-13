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


class Grades:
    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self._students:
            raise ValueError("Duplicate student")
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError("Student not in mapping")

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError("Student not in mapping")

    def get_students(self):
        """Return a sorted list of the students in the grade book one at a to,e"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s


def grade_report(course):
    """Assumes course is of type Grades"""
    report = ""
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot / num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
    return report


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

ug1 = UG("Jane Doe", 2021)
ug2 = UG("Pierce Addison", 2041)
ug3 = UG("Davidy Henry", 2003)
g1 = Grad("Billy Buckner")
g2 = Grad("Bucky F. Dent")
six_hundred = Grades()
six_hundred.add_student(ug1)
six_hundred.add_student(ug2)
six_hundred.add_student(g1)
six_hundred.add_student(g2)
for s in six_hundred.get_students():
    six_hundred.add_grade(s, 75)
six_hundred.add_grade(g1, 25)
six_hundred.add_grade(g1, 100)
six_hundred.add_student(ug3)
print(grade_report(six_hundred))

book = Grades()
book.add_student(Grad("Julie"))
book.add_student(Grad("Lisa"))
for s in book.get_students():
    print(s)
