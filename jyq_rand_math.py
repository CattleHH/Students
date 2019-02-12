'''
输入一个三位数与程序随机数比较大小
1、如果大于随机数，分别输出三位数的个位、十位、百位
2、如果等于随机数，提示“中奖”
3、如果小于随机数，将120个字符输入到文本中
（文本规则：一个字符串的长度为12，单独占一行，并且前4个是字母，后8个是数字）
'''

import random


def line():
    str_a = ''
    for i in range(4):
        rand_a = random.randrange(97, 123)
        str_a += chr(rand_a)
    # print(str_a)
    for j in range(8):
        rand_sz = random.randrange(0, 10)
        str_a += str(rand_sz)
    # print(str_a)
    return str_a

def num_game(source,total):

    while 1:

        str_num = input("请输入一个三位数,输入-1结束：")
        num = int(str_num)
        if num == -1:
            break


    # isdigit()检测字符是否由纯数字组成，返回布尔值 num.isdigit() and
        if  100 <= int(num) <= 999:
            total +=1
            print("输入{}次".format(total))
            rand_num=random.randrange(100,1000)

            if num > rand_num:
                bai = num // 100
                ge = num % 10
                shi = num%100//10
                # print(ge)
                # print(shi)
                # print(bai)
                print("输入的三位数大于随机数，个位是{}十位是{}百位是{}".format(ge,shi,bai))

            # ASCII码，大写字母65～90 小写字母97～122
            if num < rand_num:
                print("输入的三位数小于随机数,随机数是{}".format(rand_num))
                for i in range(10):
                    str_line=line()
            #         文件存储操作
                    with open('str_num.txt','a') as f:
                        f.write(str_line+'\n')

            if num == rand_num:
                source = source + 100
                print("你中奖了,分数是",source)
                print("你中奖的概率是",source/total)
        else:
            print('请按规定输入')

if __name__ == '__main__':
    total = 0
    source = 0
    num_game(source,total)