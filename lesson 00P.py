class Student:
    __num_students = 0

    def __init__(self, name, surname, year, idcard):
        self.name = name
        self.lastname = surname
        self.idcard = idcard
        self.year = year

    def __repr__(self):
        return f"ID: {self.idcard}:{self.name} {self.lastname} {self.year}-yilda tug'ilgan"

    def get_id(self):
        return self.idcard


class Fan(Student):
    __num_fan = 0

    def __init__(self, name):

        self.name = name
        Fan.__num_fan += 1
        self.students = []

    def __repr__(self):
        return f"{self.name.upper()} avtasaloni"

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]

    def __setitem__(self, index, value):
        if isinstance(value, Student):
            self.students[index] = value

    def add_student(self, *value):
        for student in value:
            if isinstance(student, Student):
                self.students.append(student)
            else:
                print("Studentni kiriting")

    def __call__(self):
        return [i for i in self.students]

    def __sub__(self, y):

        for i in self.students:
            if i.get_id() == y:
                subs=self.students.remove(i)
                print(i)
                return subs


student1 = Student('Ravshan', 'Jumanazarov', 2004, 123456)
student2 = Student('Abror', 'Muxtoraliy', 1990, 1234567)
student3 = Student('Jaloliddin', 'Rumiy', 2004, 12345678)
student4 = Student('Islom', 'Karimov', 1986, 123456789)
student5 = Student('Jasur', 'Zokirov', 2004, 1234567890)

matematika = Fan("Matematika")
matematika.add_student(student5, student4, student3, student1,student2)
matematika - student5.get_id()
matematika - student3.get_id()
print(matematika())
