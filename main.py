class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello i am {self.name}")    

    def grow_up(self):
        self.age = self.age + 1

    def print_age(self):
        print(f"age - {self.age}")

olesia_student = Student(name = "Olesia", age = 14)    
olesia_student.greeting()

matvii_student = Student(name = "Matvii", age = 14)
olesia_student.greeting()


matvii_student.print_age()
matvii_student.grow_up()
matvii_student.print_age()


