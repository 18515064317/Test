#!/usr/bin/python
# -*- coding: UTF-8 -*-

#6.题目：斐波那契数列。
# def fib(n):
#     a,b =1,1
#     for i in range(n -1):
#         a , b = b , a + b
#     return a
# print(fib(10))

# class Fiblist(object):
#     def __call__(self, num):
#         a ,b ,L = 0 , 1, []
#         for  n  in range(num):
#             L.append(a)
#             a , b = b , a + b
#         return L
# f = Fiblist()
# print (f(11))
#
# #7.题目：将一个列表的数据复制到另一个列表中。
# a = [1 , 2, 3 ,4]
# b = a[0:4]
# print(b)
#
# # 8.题目：输出 9*9 乘法口诀表。
# for i in range(1,10):
#     print
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j))

#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

# if n == 1 :
#     print ('sum:%s'%a)
# if n == 2 :
#     sum = a + a + a*10
#     print ('sum:%s' % sum)
# if n == 3 :
#     sum = a + a + a*10 + (a + a*10 + a*100)
#     print ('sum:%s' % sum)
# if n == 4 :
# #    sum = a + a + a*10 + (a + a*10 + a*100) + (a + a*10 + a*100 +a*1000)
#     sum = a*n + a*(n-1)*10 + a*(n-2)*10**2 + a*(n-3)*10**3
#     print ('sum:%s' % sum)
# a = int(input('a:'))
# n = int(input('n:'))
# tn = 0
# sn = []
# for n in range(1,n+1):
#     tn = tn + a
#     a = a*10
#     sn.append(tn)
#     print(tn)
# sum = sum(sn)
# print('sum is :%s'%sum)
# sn = max(sn)
# print(sn)

#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# def outprint(s,l):
#     if l ==0:
#         return
#     print(s[l-1])
#     outprint(s,l-1)
# s = input('shu ru s zifu:')
# l = len(s)
# outprint(s,l)

#题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
#程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推
# a = 10
# L = [10]
# for n in range(1,5):
#     a += 2
#     L.append(a)
# print(L)
# print('第五个人:%s'%L[4])
#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# x = int(input('qing shu ru yi ge shu:'))
# a = int(x /10000)
# b = int(x % 10000 /1000)
# c = int(x % 1000 / 100)
# d = int(x % 100 / 10)
# e = int(x % 10)
# #rint(a,b,c,d,e)
# if a != 0:
#     print('这是一个五位数')
#     print('逆序打印出各位数字:',e,d,c,b,a)
# if a == 0 and b != 0:
#     print('这是一个四位数')
#     print('逆序打印出各位数字:',e,d,c,b)
# if a == 0 and b == 0 and c != 0:
#     print('这是一个三位数')
#     print('逆序打印出各位数字:',e,d,c)
# if a == 0 and b == 0 and c == 0 and d != 0:
#     print('这是一个二位数')
#     print('逆序打印出各位数字:',e,d)
# if a == 0 and b == 0 and c == 0 and d == 0 and e != 0:
#     print('这是一个一位数')
#     print('逆序打印出各位数字:',e)
# if a == 0 and b == 0 and c == 0 and d == 0 and e == 0:
#     print('这数是0')

#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# x = int(input('qing shu ru yi ge wu wei shu:'))
# a = int(x /10000)
# b = int(x % 10000 /1000)
# c = int(x % 1000 / 100)
# d = int(x % 100 / 10)
# e = int(x % 10)
# if a == e and b ==d :
#     print(x,'是个回文数')
# else:
#     print(x,'不是个回文数')

#题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# Monday，Tuesday、Wednesday、Thursday、Friday、Saturday 、Sunday
# letter = input('请输入:')
# letter = letter.upper()
# if letter == 'M':
#     print ('This day is Monday')
# elif letter == 'F':
#     print ('This day is Friday')
# elif letter == 'W':
#     print ('This day is Wednesday')
# elif letter == 'T':
#     print('请继续输入下一个字母!!')
#     letter = input('请输入下一个字母:')
#     letter = letter.lower()
#     if letter == 'u':
#         print('This day is Tuesday')
#     elif letter == 'h':
#         print('This day is Thursday')
#     else:
#         print('输入错误！！')
# elif letter == 'S':
#     print('请继续输入下一个字母!!')
#     letter = input('请输入下一个字母:')
#     letter = letter.lower()
#     if letter == 'u':
#         print('This day is Sunday')
#     elif letter == 'a':
#         print('This day is Saturday')
#     else:
#         print('输入错误！！')

#题目：按相反的顺序输出列表的值。
# a  = ['asd','fff','3erre']
# for i in a[::-1]:
#     print (i)
#
# #按逗号分隔列表。
# L = [1,2,3,4,5]
# s1 = ','.join(str(n) for n in L)
# print (s1)
#
# #练习函数调用。
# def hello_world():
#     print ('hello world')
# def three_hellos():
#     for i in range(3):
#         hello_world()
# if __name__ == '__main__':
#     three_hellos()
# if __name__ == '__main__':
#     hello_world()
# #题目：文本颜色设置
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC + 'AAAAAAAAAAA')
# print (bcolors.WARNING + "警告的颜色字体?" + bcolors.HEADER + 'AAAAAAAAAAAAA')
# print (bcolors.WARNING + "警告的颜色字体?" + bcolors.OKBLUE + 'AAAAAAAAAAAAA')
# print (bcolors.WARNING + "警告的颜色字体?" + bcolors.OKGREEN + 'AAAAAAAAAAAAA')
# print (bcolors.WARNING + "警告的颜色字体?" + bcolors.FAIL + 'AAAAAAAAAAAAA')
# print (bcolors.WARNING + "警告的颜色字体?" + bcolors.BOLD + 'AAAAAAAAAAAAA')

#题目：求100之内的素数。
# 输出指定范围内的素数
# 用户输入数据
# lower = int(input("输入区间最小值: "))
# upper = int(input("输入区间最大值: "))
# for n in range(lower,upper):
#     if n > 1:
#         for i in range(2,n):
#             if  n % i ==0 : #判断是否能被整除
#                 #print("%d is not a prime number！" % n)
#                 break
#         else:
#             print("%d is a prime number！" % n)
#题目：对10个数进行排序。
#程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

# print('请输入十个数字开始!!')
# N = int(input('yao shu ru ji ge shuzi :N = '))
# L = []
# for n in range(1,N + 1):
#     L.append(int(input('请输入:')))
#     print(L)
# for i in range(N):
#         print (L[i])
# #排序
# for i in range(N-1):
#     min = i
#     for j  in range(i + 1,N):
#         if L[min] > L [j]:min = j
#     L[min],L[i] = L[i],L[min]
# print('排序之后')
# for i in range (N):
#     print(L[i])

# #题目：求输入数字的平方，如果平方运算后小于 50 则退出。
# while (1):
#     n = int(input('请输入一个数字：'))
#     if n * n < 50 :
#         print('n的平方为：%s' % n ** 2)
#         break
#     else:
#         print('n的平方shishis：%s' % n ** 2)
#         print ('请继续输入：')
# #题目：两个变量值互换。
# def changeeach(a,b):
#     a, b = b, a
#     return (a,b)
# if __name__ == '__main__':
#     x = 12
#     y = 34
#     print('x = %s ,y = %s'%(x,y))
#     x, y = changeeach(x,y)
#     print('>>>>>x = %s ,y = %s' % (x, y))
#
# #题目：数字比较
# a = int(input('请输入数字a:'))
# b = int(input('请输入数字b:'))
# if a > b:
#     print('%s > %s'%(a,b))
# if a == b:
#     print('%s == %s' % (a, b))
# else:
#     print('%s < %s' % (a, b))
# #题目：使用lambda来创建匿名函数。
# la = lambda x,y:x*y
# x = int(input('X:'))
# y = int(input('Y:'))
# print(la(x,y))
# lambda基础
# lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象，见证一下：
# >>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# >>> print filter(lambda x: x % 3 == 0, foo)
# [18, 9, 24, 12, 27]
# >>> print map(lambda x: x * 2 + 10, foo)
# [14, 46, 28, 54, 44, 58, 26, 34, 64]
# >>> print reduce(lambda x, y: x + y, foo)
# 139
# #题目：输出一个随机数。
# import random
# print(random.randint(0, 99))
# #题目：学习使用按位与 & 。
# a = 77
# b = a & 3
# print ('a & b = %d' % b)
# b &= 7
# print ('a & b = %d' % b)
#题目：画图，学用circle画圆形
# import turtle
# turtle.title("画圆")
# turtle.setup(800,600,0,0)
# pen=turtle.Turtle()
# pen.color("yellow")
# pen.width(10)
# pen.shape("turtle")
# pen.speed(1)
# pen.circle(100)
# def drawline(n):
#     t=turtle.Pen()
#     t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
#     t.begin_fill()   #开始填充颜色
#     for i in range(n): #任意边形
#         t.forward(200)
#         t.left(360/n)
#     t.end_fill()    #结束填充颜色
# drawline(4)
#画布就是turtle为我们展开用于绘图区域，我们可以设置它的大小和初始位置。
#设置画布大小
# turtle.screensize(canvwidth=900, canvheight=800, bg='red')    #，参数分别为画布的宽(单位像素), 高, 背景颜色。
# turtle.setup(width=800,height=800, startx=100, starty=100)
import turtle
import time
# #太阳花
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for _ in range(36):
#     turtle.forward(300)
#     turtle.left(170)
# turtle.end_fill()
# turtle.mainloop()
# #五角星
# turtle.color("red")
# turtle.pensize(4)
# turtle.pencolor('yellow')
# turtle.begin_fill()
# for _ in range(5):
#     turtle.forward(200)
#     turtle.left(144)
# turtle.end_fill()
# turtle.mainloop()
#贪吃蛇
def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2)  # 直线前进
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)
if __name__ == "__main__":
   turtle.setup(1500, 1400, 0, 0)
   turtle.pensize(30)  # 画笔尺寸
   turtle.pencolor("green")
   turtle.seth(-40)    # 前进的方向
   drawSnake(70, 80, 3, 15)

# tutle = turtle.screensize(400,400,'yellow')
# turtle.circle(50)
# x0 = 263
# y0 = 263
# y1 = 275
# x1 = 275
# for i in range(19):
#





