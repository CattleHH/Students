
# 实心矩形
# for i in range(5):
#     print('* '*5)

# for i in range(5):
#     for j in range(5):
#         print('* ',end='')
#     print('')
#   空心矩形
# for i in range(5):
#
#    for j in range(5):
#        if i == 0 or i==4 or j == 0 or j == 4:
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')s
#    print()

# 直角三角形
# for i in range(5):
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# 空心直角三角形
# for i in range(5):
#     for j in range(i+1):
#         if  i == 0 or i == 4 or j == 0 or j == i:
#            print('* ',end='')
#         else:
#             print('  ',end='')
#     print()

# 倒直角三角形
# for i in range(5):
#     for j in range(5-i):
#         print('* ',end='')
#     print()



# 倒直角三角形反向
# for i in range(5):
#     for j in range(5-i):
#         print('  ',end='')
#     for m in range(i+1):
#         print('* ', end='')
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print('  ',end='')
#     for m in range(5-i):
#         print('* ', end='')
#     print()

# 正三角形
# for i in range(5):
#     for j in range(5-i):
#         print(end=' ')
#     for k in range(i+1):
#         print('* ',end='')
#     print()

# 空心正三角形
# import time
# for i in range(5):
#     for j in range(5-i):
#         print(end=' ')
#     for k in range(i+1):
#         if i == 0  or i == 4 or k == 0 or k == 4 or k == i:
#            print('* ',end='')
#            time.sleep(1)
#         else :
#             print('  ',end='')
#     print('')

# 倒正三角形
# for i in range(5):
#     for j in range(i+1):
#         print('=',end='')
#     for k in range(5-i):
#         print('*',end=' ')
#     print()

# 空心倒正三角形
# import  time
# for i in range(5):
#     for j in range(i+1):
#         print('=',end='')
#         # time.sleep(1)
#     for k in range(5-i):
#         if i == 0 or i == 4 or k == 0 or k == (4-i):
#            print('*',end=' ')
#            # time.sleep(1)
#         else:
#             print(' ',end=' ')
#     print()

# 字母A
# for i in range(5):
#     for j in range(5-i):
#         print(' ',end='')
#     for k in range(i+1):
#         if i == 0 or i == 3 or k == 0 or k == 4 or k == i:
#            print('*',end=' ')
#         else:
#             print('  ',end='')
#     print()


# 菱形
# for i in range(4):
#     for j in range(5-i):
#         print(end=' ')
#     for k in range(i+1):
#         print('* ',end='')
#     print()
# for i in range(5):
#     for j in range(i+1):
#         print(end=' ')
#     for k in range(5-i):
#         print('* ',end='')
#     print()


# 空心菱形
# for i in range(4):
#     for j in range(5-i):
#         print(end=' ')
#     for k in range(i+1):
#         if i == 0   or k == 0 or k == i:
#            print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# for i in range(5):
#     for j in range(i+1):
#         print(end=' ')
#     for k in range(5-i):
#         if i == 4 or k == 0 or k == 4 or k == 4-i :
#            print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# 实心梯形
# for i in range(5):
#     for m in range(5-i):
#         print(' ',end='')
#     for j in range (i+4):
#         print('*',end=' ')
#     print()

# 空心梯形
# for i in range(5):
#     for m in range(4-i):
#         print('=',end='')
#     for j in range (i+4):
#         if i == 0 or i == 4 or j == 0 or j == i+3:
#            print('*',end=' ')
#         else:
#             print('=',end=' ')
#     print()

# D
# for i in range(4):
#     for j in range(2):
#       if i == 0 or i == 3 or j == 0:
#          print('*', end=' ')
#     for m in range(3):
#       if i == 1 and m == 2:
#          print('*',end='')
#       elif i == 2 and m == 2:
#           print('*', end='')
#       print('',end=' ')
#     print()

# 大B
# for i in range(3):
#     for j in range(2):
#       if i == 0:
#           print('*', end=' ')
#       elif j == 0  and i < 3:
#          print('*', end=' ')
#     for m in range(2):
#       if i == 1 and m == 1:
#          print('*',end='')
#       elif i == 2 and m == 1:
#          print('*', end='')
#       print(' ',end=' ')
#     print()
# for i in range(4):
#     for j in range(2):
#       if i == 0 or i == 3 or j == 0:
#          print('*', end=' ')
#     for m in range(3):
#       if i == 1 and m == 2:
#          print('*',end='')
#       elif i == 2 and m == 2:
#           print('*', end='')
#       print('',end=' ')
#     print()

# 小B
# for i in range(2):
#     for j in range(2):
#       if i == 0:
#           print('*', end=' ')
#       elif j == 0  and i < 2:
#          print('*', end=' ')
#     for m in range(2):
#       if i == 1 and m == 1:
#          print('*',end='')
#       print(' ',end=' ')
#     print()
# for i in range(3):
#     for j in range(2):
#       if i == 0 or i == 2 or j == 0:
#          print('*', end=' ')
#     for m in range(2):
#       if i == 1 and m == 1:
#          print('*',end='')
#       elif i == 2 and m == 2:
#          print('*', end='')
#       print(' ',end=' ')
#     print()

# R
for i in range(3):
    for j in range(2):
      if i == 0:
          print('*', end=' ')
      elif j == 0  and i < 3:
         print('*', end=' ')
    for m in range(2):
      if i == 1 and m == 1:
         print('*',end='')
      elif i == 2 and m == 1:
         print('*', end='')
      print(' ',end=' ')
    print()
for i in range(3):
    for j in range(2):
      if i == 0  or j == 0:
         print('*', end=' ')
    for m in range(i+2):
      if i == 1 and m == 2:
         print('*',end='')
      elif i == 2 and m == 3:
          print('*', end='')
      print('',end=' ')
    print()

