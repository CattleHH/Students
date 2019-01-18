# def digui(num):
#     print(num)
#     if num > 0:
#         digui(num-1)
#         print('-')
#     else:
#         print('='*20)
#     print(num)
#
# digui(3)



def test1(n):
    print("level %d" % n)
    if n<4  :   test1(n+1)
    print("level %d" % n)

def test2(n):
    print("level %d" % n)
    a = [1,2]
    for key in a:
        if key<n:    test2(n-1)
        print("level %d" % key)

def test3(n):
    print("level %d" % n)
    a = [1,2]
    for key in a:
        if key<n:    test3(n-1)
        else :     print("level %d" % key)

test1(1)
print('='*10)
test2(2)
print('*'*10)
test3(2)
