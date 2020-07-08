Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help(inpit)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(inpit)
NameError: name 'inpit' is not defined
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> input("input your name:")
input your name:123
'123'
>>> user=input("name")
name123
>>> user
'123'
>>> "i like %s" % "Python"
'i like Python'
>>> "i like %s" % "Pascal"  # %s为一个占位符，%后接与之对应类型的对象，常用的还有%d、%f
'i like Pascal'
>>> a="%d years old" % 22
>>> print(a)
22 years old
>>> print("suzhu is more than %d years, %s lives in here" % (2500,"qiwisr"))
suzhu is more than 2500 years, qiwisr lives in here
>>> #以上设置了多个占位符
>>> print("today's temperature is %.2f" % 12.35)
today's temperature is 12.35
>>> print("today's temperature is %+.2f" % 12.235)
today's temperature is +12.23
>>> #以上对于浮点数字的打印输出，还可以限定输出的小数位数和其它样式，注意，上面的例子中，没有实现四舍五入的操作。只是截取
>>> s1 = "i like {}".format("pathon")
>>> s1
'i like pathon'
>>> s2="suzhu is more than {} years. {} lives in here.".format(2500,"qiwisr")
>>> s2
'suzhu is more than 2500 years. qiwisr lives in here.'
>>> #简便方法，Python 非常提倡的 string.format()的格式化方法，其中 {} 作为占位符，只需要将对应的东西，按照顺序在 format 后面的括号中排列好，分别对应占位符 {} 即可。还可以如下操作：
>>> print"suzhu is more than {year} years. {name} lives in here.".format(year=2500,name="qiwsir")
SyntaxError: invalid syntax
>>> print"suzhu is more than {year} years. {name} lives in here.".format(year=2500,name="qiwsir")
SyntaxError: invalid syntax
>>> print("suzhu is more than {year} years,{name} lives in here.".format(year=2500,name="qiwsir"))
suzhu is more than 2500 years,qiwsir lives in here.
>>> #另一种方法如下：
>>> lang="Python"
>>> print("i love %(program)s"%{"program":lang})
i love Python
>>> dir(str)  #查看字符串方法
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.isalpha)  #查看某个具体的使用方法
Help on method_descriptor:

isalpha(self, /)
    Return True if the string is an alphabetic string, False otherwise.
    
    A string is alphabetic if all characters in the string are alphabetic and there
    is at least one character in the string.

>>> "Python".isalpha()  #字符串全是字母，应该返回ture
True
>>> "2Python".isalpha()  #字符串含非字母，返回false
False
>>> #split函数将字符串根据某个分割符进行分割，eg如下
>>> a="i love Python"
>>> a.split(" ")
['i', 'love', 'Python']
>>> #得到一个名字叫做列表（list）的返回值
>>> b="www.itdiffer.com"
>>> b.split(".")
['www', 'itdiffer', 'com']
>>> #去掉字符串两头的空格：S.strip() 去掉字符串的左右空格、S.lstrip() 去掉字符串的左边空格、S.rstrip() 去掉字符串的右边空格。eg如下：
>>> a="  hello  "   #两边有空格
>>> a.strip()
'hello'
>>> b
'www.itdiffer.com'
>>> a
'  hello  '
>>> #特别注意，原来的值没有变化，而是新返回了一个结果
>>> a.lstrip()  #去掉左边的空格
'hello  '
>>> #字符大小写的转换（内建函数实现）：S.upper() #S 中的字母大写、S.lower() #S 中的字母小写、S.capitalize() # 首字母大写、S.isupper() #S 中的字母是否全是大写、S.islower() #S 中的字母是否全是小写、S.istitle() #判断每个单词的第一个字母是否为大写，也可以将所有单词的第一个字母改成大写
>>> a="qiwsir,Python"
>>> a.upper()
'QIWSIR,PYTHON'
>>> a     #原数据对象没有改变
'qiwsir,Python'
>>> b=a.upper()
>>> b
'QIWSIR,PYTHON'
>>> c=b.lower()
>>> c
'qiwsir,python'
>>> a.capitalize()    #首字母大写
'Qiwsir,python'
>>> a
'qiwsir,Python'
>>> b=a.capitalize()
>>> b
'Qiwsir,python'
>>> a.istitle()
False
>>> a="Qiwsir Python"
>>> a.istitle()
True
>>> a.isupper()  #判断是否全大写
False
>>> a.upper().isupper()
True
>>> a.islower()
False
>>> a.lower().islower()
True
>>> a="this is a book"
>>> a.istitle()
False
>>> b=a.title()
>>> b
'This Is A Book'
>>> b.istitle()
True
>>> b
'This Is A Book'
>>> b="www.itdiffer.com"
>>> b
'www.itdiffer.com'
>>> c=b.spilt(".")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    c=b.spilt(".")
AttributeError: 'str' object has no attribute 'spilt'
>>> c=b.split(".")
>>> c
['www', 'itdiffer', 'com']
>>> ".".join(c)
'www.itdiffer.com'
>>> "*".join(c)
'www*itdiffer*com'
>>> #join可以将列表中的每个字符（串）元素拼接成一个字符串，并且用某个符号连接，+能够拼接字符串，但不是什么情况下都能够如愿的，这里可用，但麻烦