# 13
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print("Person attributes:\n"
              "\tfirstname: {}\n"
              "\tlastname: {}\n"
              "\tage: {}".format(self.firstname,
                                 self.lastname,
                                 self.age))


class Student(Person):
    studentsCount = 0

    def __init__(self, firstname, lastname, age, recordBook):
        Person.__init__(self, firstname, lastname, age)
        self.studentID = Student.studentsCount
        Student.studentsCount += 1
        self.recordBook = recordBook

    def display(self):
        Person.display(self)
        print("\tstudentID: {}\n"
              "\trecordBook:\n"
              "\t\t5: {}\n"
              "\t\t4: {}\n"
              "\t\t3: {}\n"
              "\t\t2: {}".format(self.studentID,
                                 self.recordBook[3],  # 5
                                 self.recordBook[2],  # 4
                                 self.recordBook[1],  # 3
                                 self.recordBook[0]))  # 2


student1 = Student("Vasya", "Pupkin", 18, [12, 43, 654, 5])
student2 = Student("Vasya1", "Pu3pkin", 181, [12333, 433, 654, 5])
student3 = Student("Vas12ya", "Pu33pkin", 118, [132, 433, 6524, 5])
student1.display()
student2.display()
student3.display()


# 14

class Professor(Person):
    professorsCount = 0

    def __init__(self, firstname, lastname, age, degree):
        Person.__init__(self, firstname, lastname, age)
        self.professorID = Professor.professorsCount
        Professor.professorsCount += 1
        self.degree = degree

    def display(self):
        Person.display(self)
        print("\tprofessorID: {}\n"
              "\tdegree: {}".format(self.professorID,
                                    self.degree))


prof1 = Professor("Meow", "Neko-kun1", 20, "docent")
prof2 = Professor("Meow", "Neko-kun2", 20, "123")
prof3 = Professor("Meow", "Neko-kun3", 20, "1233")

prof1.display()
prof2.display()
prof3.display()
