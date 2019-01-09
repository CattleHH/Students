# 魔法函数可以自己重构，便于实现自定义的一些功能
# 达到某些特定条件，魔法函数会自动触发，无需手动调用
class Student():
    def __init__(self,name):
        self._name=name
        print(str(self._name))


    # __gt__使用大于比较的时候触发的魔法函数
    def __gt__(self,obj):
        # self和obj代表两个对象
        # self代表自己，obj代表第二个对象
        # 不加._name比较结果显示对象
        print("哈哈哈，{0}会比{1} 大吗".format(self._name,obj._name))
        # print("哈哈哈，{0}会比{1} 大吗".format(self, obj))
        return self._name > obj._name

# s=Student()
s1=Student("one")
s2=Student("two")
# print(repr(s1)>repr(s2))
#print(str(s1)>str(s2))
print(s1>s2)