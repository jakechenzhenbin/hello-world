#-*- coding:utf-8 -*-
#contact: 787872498@qq.com
#file: test_01.py
#time: 2020/5/25 17:36

# print("趁自己肯定就付款即可")
#
# class MyClass:
#     i = 123456
#     def a(self):
#         return "hello wolrd"
# x = MyClass()
# print(x.i)
# print(x.a())
# import random
# print(random.random())
# n = 0
# while n < 5:
#     a = random.randint(1,10)
#     b = int(input("输入一个数字："))
#     if a == b:
#         print("您猜对了")
#         break
#     elif a < b:
#         print("您这边猜大了")
#         print("结果是：{}".format(a))
#     elif a > b:
#         print("您这边猜小了")
#         print("结果是：{}".format(a))
#     n += 1
# else:
#     print("您这边已经猜了五次了")

# name = 'hello python'
# print(name[5])
# print(name.find('p',7,len(name)))
# print(name.index('p',7,len(name)))
# name.find()
# len(name)
# format()
# name.upper()

# l = ['chen','zhen','bin',10086,1994]
# print(l)
# print(id(l))
# l.append('jia min')
# print(l)
# print(id(l))
# l[2] = 'yang'
# print(l[0:-2])
# print(l + ['sd',65,85,'jkl'])
# a = ['yang','jia','min',1992,1688]
# print([l,a])

# t = ('chen','zhen','bin',10086,1994)
# print(type(t))
# l = list(t)
# print(type(l))
# print(l)

# t = 'abc','czb',5,9
# print(type(t))

# t = ('czb',)
# print(type(t))

# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# print(tup1 + tup2)
# print((tup1,tup2))
# del tup1
# print(tup1)

# t1=(1,2,3)
# for i in range(1,5):
#     t2=(i,)
#     t1=t1+t2
# print(t1)

# l = ['chen','zhen','bin',10086,1994]
# print(l.index(10086))
# l.insert()
# l.pop(2)
# print(l)

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First',564:441}
# print(dict['Name'])
# dict[564] = '超玩会'
# print(dict)
# print(type(dict))
# # del dict
# # print(dict['Class'])
# dict = str(dict)
# print(dict)
# print(type(dict))

# l = ['chen','zhen','bin',10086,1994,'bin']
# l.remove('bin')
# print(l)
# del l[1]
# print(l)
# l1 = l.pop(3)
# print(l)
# print(l1)

# age = int(input("请输入你家狗狗的年龄: "))
# def dog(age):
#     if age <= 0:
#         print("你是在逗我吧!")
#         print()
#     elif age == 1:
#         print("相当于 14 岁的人。")
#     elif age == 2:
#         print("相当于 22 岁的人。")
#         print()
#     elif age > 2:
#         human = 22 + (age - 2) * 5
#         print("对应人类年龄: ", human)
#     ### 退出提示
#     input("点击 enter 键退出")
# dog(int(input("请输入你家狗狗的年龄: ")))

# print(8==9)

# sum = 0
# i = 1
# while i < 11:
#     sum = sum +i
#     i = i + 1
#     print(sum)

# sum = 0
# while sum < 4:
#     print("sum的值是{}，并且小于4".format(sum))
#     sum = sum + 1
# else:
#     print("sum的值是{}，并且大于或等于4".format(sum))
# print(tuple(range(5)))
# sum = 0
# for n in range(0,101):
#     sum = sum + n
# print(sum)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(j,i,j*i),end=" ")
#     print()

# def sum(x,y):
#     print(x+y)
# sum(1,9)

# def printme(str):
#     print(str)
#     return
# printme(str="菜鸟教程")

# def printinfo(arg1, *vartuple):
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
# printinfo(70, 60, 50,401,"chenzhen",[2,8,9,'vbknjkdf',[1,6,8]],('fgdjik',8,9,3))

# def printinfo(arg1, *vartuple):
#     print("输出: ")
#     # print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# printinfo(10)
# printinfo(70, 60, 50)

# def printinfo(arg1, **vardict):
#     print("输出: ")
#     # print(arg1)
#     print(vardict)
# printinfo(1, a=2, b=3)

# sum = lambda arg1, vardict: arg1 + vardict
# print(sum(3,9))

# sum = lambda arg1, arg2: arg1 / arg2
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))

# g= lambda x=0,y=0 : x**2+y**2
# print(g(2,3))
# print(g(5))
# print(g(3,y=5))

# print((lambda x,y:x+y)(5,6))

# print(list(map(lambda x:x*x, range(1,11))))
# print(sum(map(lambda x:x*x, range(1,4))))
# print(tuple(filter(lambda x:x%2==0, range(1,11))))

# from functools import reduce
# print(reduce(lambda x,y:x+y, range(1,11),300))

# def add(n):
#     return lambda x:x*n
# add2 = add(5)
# print(add2(15))

# print((lambda x,y:x+y)(9,12))
# print((lambda x,y,z:(x+8)*y-z))
# print((lambda x,y,z:(x+8)*y-z)(8, 9, z=10))




# l = [1,2,3,4]
# l.append(5)
# print(l)
# l[len(l):]= 5
# print(l)
# l[3] = 9
# print(l)

# l = '   sdkfjk '
# print(l.strip())

# s = [3,5,6]
# print([x*x for x in s])
# print([x*3 for x in s if x>4])

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k in knights.items():
#     print(k)

# fo = open("D:/shuju.txt",'r+')
# for i in fo.readlines():
#     l = i.strip()
#     print('输出的结果为：',l)
# fo.close()
# fo1 = fo.read(10)
# print(fo1)

# with open('D:/shuju.txt','r',encoding='utf-8') as led:
#     print(led.readlines())

# try:
#     f = open('D:/dfk.txt', 'r')
# except FileNotFoundError as e:
#     print('cannot open:{}'.format(e))
# else:
#     print('抛出异常')
#     f.close()
# finally:
#     print('不管发生什么都会执行')

# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


# class Persion:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# student = Persion('chen','chenzhen')
# print(student.name)
# print(student.score)


# class Person:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
        # print('用自己的myself，打开那个{}的{}'.format(self.x,self.y))
        # print('用自己的myself，打开那个{}的{}'.format(a.x,a.y))
        # sum = self.x + self.y
        # return sum
#     def square(self,z=20):
#         self.z = z
#         squr = pow(self.x, 2) + pow(self.y, 2) + z
#         return squr
#     def add_square(self):
#         c = self.add() + self.square() + self.z
#         return c
# student = Person(3, 4)
# print(student.add())
# print(student.square())
# print('--------- 我是可爱的分割线-----------')
# print(student.add_square())
# print(student.z)


# class Box():
#     def __init__(self, boxname, size, color):
#         self.bxname = boxname
#         self.sze = size
#         self.clor = color
#     def open(self, a):
#         print('-->用自己的myself，打开那个{},{}的{}'.format(a.clor, a.sze, a.bxname))
#         print('-->用类自己的self，打开那个{},{}的{}'.format(self.clor, self.sze, self.bxname))
#     def close(self):
#         print('-->关闭%s，谢谢' % self.bxname)
# b = Box('魔盒', '14m', '红色')
# b.close()
# b.open(b)


# while True:
#     try:
#         num = int(input('请自觉输入：'))
#     except Exception as f:
#         print('输入的不是整数：{}'.format(f))
#         continue
#     if num == 0:
#         print("输入的数字是0")
#     elif num%2 == 0:
#         print("是偶数")
#     else:
#         print('是奇数')
#     break

# class Solution:
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target
#     def twoSum(self,a):
#         for i in range(len(a.nums)):
#             for j in range(i+1,len(a.nums)):
#                 if a.nums[i] + a.nums[j] == a.target:
#                     print(i,j)
#                 else:
#                     break
# sum = Solution([2,8,19,25],27)
# sum.twoSum(sum)


# class Solution:
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target
#     def twoSum(self):
#         for i in range(len(self.nums)-1,-1,-1):
#             if self.nums[i] == self.target:
#                 self.nums.pop(i)
#             else:
#                 continue
#         print(len(self.nums))
# sum = Solution([2,8,25,99,65,25,19,25,26,27],25)
# sum.twoSum()


# class Solution:
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target
#     def twoSum(self):
#         try:
#             for i in range(len(self.nums)):
#                 if self.nums[i] == self.target:
#                     self.nums.pop(i)
#                 else:
#                     continue
#         except Exception as f:
#             print(f)
#         print(len(self.nums))
# sum = Solution([2,8,25,99,65,25,19,25,26,27],25)
# sum.twoSum()

# class Soultion:
#     def __init__(self,l,a):
#         self.__l = l
#         self.a = a
#     def print_score(self):
#         return ("输出的结果为：{}".format(self.__l))
#     def get_name(self):
#         return ("一定要输出：{}".format(self.__l))
    # def searchInsert(self):
    #     if self.a in self.l:
    #         return self.l.index(self.a)
    #     else:
    #         self.l.append(self.a)
    #         self.l.sort()
    #         return self.l.index(self.a)
# s = Soultion([1,3,5,6,18,10,5,9,13],17)
# print(s.searchInsert())
# print(s.print_score())
# print(s.get_name())

# class Soution:
#     def lengFenge(self,s):
#         if s.split(s) == []:
#             return 0
#         else:
#             p = s.split()
#             return len(p[-1])
# f = Soution()
# print(f.lengFenge('hello world chen zhen'))

# import requests
#
# url = "http://192.168.3.165:89/sale-publish-ebay/ebayTemplate/checkSpecialCategory?primaryCategoryId=117044"
# payload = {'primaryCategoryId':117044}
# headers = {
#   'Content-Type': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data = payload)
# print(response.text.encode('utf8'))


# from random import randrange, randint, sample

# def display(balls):
    """
    输出列表中的双色球号码
    """
    # for index, ball in enumerate(balls):
    #     if index == len(balls) - 1:
    #         print('|', end=' ')
    #     print('%02d' % ball, end=' ')
    # print()

# def random_select():
    """
    随机选择一组号码
    """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls
# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())
# if __name__ == '__main__':
#     main()




































