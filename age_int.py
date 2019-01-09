class Person():

    def fget(self):
        print("fget")
        return self._age * 2
    def fset(self,age):
        print("fset")
        self._age=int(age)

    def fdel(self):
        print("fdef")
    age=property(fget,fset,fdel,"对年龄取整")

p = Person()
p.age=6.78
print(p.age)


