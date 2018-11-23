class A():
    name="aaa"
    age=19
    def __init__(self):
        self.name="init"
        self.age=18
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name="bbbb"
    age=17


a=A()
a.say()
A.say(a)
A.say(A)
A.say(B)