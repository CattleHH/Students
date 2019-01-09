class Person():
    name = "DaNa"
    age = 18
    def eat(self):
        print("eating...")

    def drink(self):
        print("drinking...")

    def sleep(self):
        print("sleeping...")

class Teacher(Person):
    def work(self):
        print("work...")
class Student(Person):
    def study(self):
        print("study...")
class Tutor(Teacher,Student):
    pass

t=Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)