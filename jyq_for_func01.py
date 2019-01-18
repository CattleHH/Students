while 1:
    # 实心矩形
    def s_jx():
         for i in range(5):
            for j in range(5):
                print('* ',end='')
            print('')
    #   空心矩形
    def k_jx():
        for i in range(5):
           for j in range(5):
               if i == 0 or i==4 or j == 0 or j == 4:
                   print('*',end=' ')
               else:
                   print(' ',end=' ')
           print()
    # 直角三角形
    def s_sjx():
        for i in range(5):
            for j in range(i+1):
                print('* ',end='')
            print()

    # 空心直角三角形
    def k_sjx():
        for i in range(5):
            for j in range(i+1):
                if  i == 0 or i == 4 or j == 0 or j == i:
                   print('* ',end='')
                else:
                    print('  ',end='')
            print()

    print('输入-1结束！')
    shape = input('请输入实心矩形、空心矩形、实心三角形或空心三角形后回车：')

    if shape == -1:
        break
    elif shape == '实心矩形':
        s_jx()
    elif shape == '空心矩形':
        k_jx()
    elif shape == '实心三角形':
        s_sjx()
    elif shape == '空心三角形':
        k_sjx()
    else:
        print('找不到匹配的图形')

