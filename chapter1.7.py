Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lang="study Python"
>>> lang[2]
'u'
>>> "study Python"[2]
'u'
>>> lang[0]
's'
>>> lang.index(" ")
5
>>> lang
'study Python'
>>> lang[2:8]
'udy Py'
>>> lang[1:9]     #得到左边数至右边前一位数的对应字符
'tudy Pyt'
>>> lang[:10]     #分号之前或者之后不写表示从第一个至右边数的前一个（左边不写），或者从左边数至最后一个（右边不写）
'study Pyth'
>>> lang[1:11]
'tudy Pytho'
>>> lang[1:]
'tudy Python'
>>> lang[1:12]     #可以在右边写入大于11的数来得到第11位对应的字符。但不提倡
'tudy Python'
>>> c=lang[:]      #左右两边都不写时，相当于c和lang两个变量指向的是同一个对象，两个变量地址相同
>>> id(c)
61430424
>>> id(lang)
61430424
>>> c
'study Python'
>>> lang
'study Python'
>>> c.index(" ")
5
>>> lang="study Python"
>>> c=lang
>>> c
'study Python'
>>> lang
'study Python'
>>> c.index(" ")
5
>>> lang.index(" ")
5
>>> #len()求序列长度、+连接两个序列、*重复序列元素、in判断元素是否在序列中、max（）返回最大值、min（）返回最小值、cmp（str1,str2）比较两个序列值是否相同
>>> str1="123"
>>> str2="456"
>>> str1+str2
'123456'
>>> str1+"-->"+str2
'123-->456'
>>> "1"in str1
True
>>> "7" in str1
False
>>> max(str1)
'3'
>>> max(str2)
'6'
>>> min(str1)
'1'
>>> min(str2)       #最大最小值是按照其对应ASCII码来比较的，cmp（）中也是
'4'
>>> cmp(str1,str2)  #将两个字符串进行比较，也是首先将字符串中的符号转化为对一个的数字，然后比较。如果返回的数值小于零，说明第一个小于第二个，等于 0，则两个相等，大于 0，第一个大于第二个。且在字符串的比较中，是两个字符串的第一个字符先比较，如果相等，就比较下一个，如果不相等，就返回结果。直到最后，如果还相等，就返回 0。位数不够时，按照没有处理（注意，没有不是 0，0 在 ASCII 中对应的是 NUL），位数多的那个天然大了
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    cmp(str1,str2)  #将两个字符串进行比较，也是首先将字符串中的符号转化为对一个的数字，然后比较。如果返回的数值小于零，说明第一个小于第二个，等于 0，则两个相等，大于 0，第一个大于第二个。且在字符串的比较中，是两个字符串的第一个字符先比较，如果相等，就比较下一个，如果不相等，就返回结果。直到最后，如果还相等，就返回 0。位数不够时，按照没有处理（注意，没有不是 0，0 在 ASCII 中对应的是 NUL），位数多的那个天然大了
NameError: name 'cmp' is not defined
>>> import operator   #Python 3中移除了cmp()函数，但是提供了六个比较丰富的比较运算，此处是要先导入运算符模块
>>> operator.gt(1,2)  #意思是大于
False
>>> eperator.ge(1,2)  #意思是大于等于
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    eperator.ge(1,2)  #意思是大于等于
NameError: name 'eperator' is not defined
>>> operator.ge(1,2)  #意思是大于等于
False
>>> operator.eq(1,2)  #意思是等于
False
>>> operator.le(1,2)  #意思是小于等于
True
>>> operate.lt(1,2)   #意思是小于
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    operate.lt(1,2)   #意思是小于
NameError: name 'operate' is not defined
>>> operator.lt(1,2)  #意思是小于
True
>>> operator.lt(str1,str2)
True
>>> ord("a")
97
>>> ord("b")   #ord()是一个内建函数，能够返回某个字符（注意，是一个字符，不是多个字符组成的串）所对一个的 ASCII 值（是十进制的）
98
>>> chr(97)    #反过来，根据整数值得到相应字符，可以使用 chr()
'a'
>>> operator.eq("aaa","abc")
False
>>> operator.ge("123","23")
False
>>> operator.ge(123,23)
True
>>> str1*3   #字符串中的“乘法”，这个乘法，就是重复那个字符串的含义
'123123123'
>>> print("'-'*20")
'-'*20
>>> print("-"*20)
--------------------
>>> print"-"*20
SyntaxError: invalid syntax
>>> len(str1)   #求字符串长度
3
>>> m=len(str1)
>>> m
3
>>> type(m)
<class 'int'>
>>> 