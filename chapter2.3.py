#! /usr/bin/env python     #这一行是必须写的，它能够引导程序找到 Python 的解析器，也就是说，不管你这个文件保存在什么地方，这个程序都能执行，而不用制定 Python 的安装路径。（unix系统而言）
#coding:utf-8              #这一行是告诉 Python，本程序采用的编码格式是 utf-8,只有有了上面这句话，后面的程序中才能写汉字，否则就会报错了

print("请输入任意一个整数数字：")

number=int(input())

if number==10:
    print("您输入的数字是:%d"%number)
    print("you are smart.")
elif number>10:
    print("您输入的数字是:%d"%number)
    print("this number is more than 10.")
elif number<10:
    print("您输如的数字是:%d"%number)
    print("this number is less than 10.")
else:
    print("are you a human?")
