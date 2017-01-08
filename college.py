
class CollegePerson:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Faculty(CollegePerson):
    def __init__(self, name):
        CollegePerson.__init__(self, name)
        self.classes = []

    def teach_a_class(self, college_class):
        self.classes.append(college_class)

class Student(CollegePerson):
    def __init__(self, name):
        CollegePerson.__init__(self, name)
        self.classes = []

    def enrole_in_class(self, college_class):
        self.classes.append(college_class)
        college_class.add_a_student(self)

class CollegeClass:
    def __init__(self, name, professor):
        self.name = name
        self.professor = professor
        self.grade_book = {}
        professor.teach_a_class(self)

    def add_a_student(self, student):
        if not student.name in self.grade_book:
            self.grade_book[student.name] = "I"

    def __str__(self):
        str = "Class Name: " + self.name + "\n"
        str += "Professor: " + self.professor.name + "\n"
        for key, value in self.grade_book.items():
            str += "Student: " + key + " Grade: " + value + '\n'
        str += "\n"
        return str


prof_1 = Faculty("John Koch")
prof_2 = Faculty("Joe Parker")
stud_1 = Student("John Salwitz")
stud_2 = Student("John Novak")
class_1 = CollegeClass("Data Structures", prof_2)
class_2 = CollegeClass("Cobol", prof_1)
stud_1.enrole_in_class(class_1)
stud_1.enrole_in_class(class_2)
stud_2.enrole_in_class(class_1)
print(class_1)
print(class_2)