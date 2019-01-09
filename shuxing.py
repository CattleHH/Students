# class Person():
#       def fget(self):
#         return self._name*2
#       def fset(self,name):
#         self._name = name.upper()
#
#       def fdel(self):
#         print("fdef")
#       name=property(fget,fset,fdel,"miingzi")
#
# p = Person()
# p.name = "tuLing"
# print(p.name)


class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)

    def intro(self):
        print("my name is {0}".format(self.name))

    def setName(self,name):
        self.name = name.upper()


s1 = Student("DaNa liu",18)
s2 = Student("michi stangle",18)

s1.intro()
s2.intro()

# print(s1.__dir__())