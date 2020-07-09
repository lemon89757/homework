Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="老齐"
>>> name
'老齐'
>>> a=[]
>>> type(a)
<class 'list'>
>>> bool(a)   #用内置函数 bool()看看 list 类型的变量 a 的布尔值，因为是空的，所以为 False
False
>>> print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> print(a)
[]
>>> #bool()是一个布尔函数，这个东西后面会详述。它的作用就是来判断一个对象是“真”还是“空”（假）。如果想上面例子那样，list 中什么也没有，就是空的，用 bool()函数来判断，得到 False，从而显示它是空的。
>>> 
>>> 
>>> a=['2',3,'github.io']
>>> a
['2', 3, 'github.io']
>>> type(a)
<class 'list'>
>>> bool(a)
True
>>> print(a)
['2', 3, 'github.io']
>>> #list 中的元素是任意类型的，可以是 int,str，甚至还可以是 list，乃至于是以后要学的 dict 等
>>> 
>>> #索引和切片
>>> str_1="qiwsir.github.io"
>>> str_1[2]
'w'
>>> str_1[:4]
'qiws'
>>> str_1[3:9]
'sir.gi'
>>> str_1
'qiwsir.github.io'
>>> list_1=['2',3,'lemon']
>>> list_1[0]
'2'
>>> #list中是以元素为单位，不是以字符为单位进行索引了，且索引序号也是从 0 开始
>>> list_1[1]
3
>>> list_[:2]   #跟str中的类似，切片的范围是：包含开始位置，到结束位置之前
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list_[:2]   #跟str中的类似，切片的范围是：包含开始位置，到结束位置之前
NameError: name 'list_' is not defined
>>> list_1[:2]   #跟str中的类似，切片的范围是：包含开始位置，到结束位置之前
['2', 3]
>>> list_1[1:]
[3, 'lemon']
>>> str_1
'qiwsir.github.io'
>>> str_1.index("q")
0
>>> list_1
['2', 3, 'lemon']
>>> list_1.index['lemon']
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list_1.index['lemon']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list_1,index('lemon')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list_1,index('lemon')
NameError: name 'index' is not defined
>>> list_1.index('lemon')
2
>>> list_1[-1]
'lemon'
>>> str_1[-1]    #此外，还有一种编号方式，就是从右边开始，右边第一个可以编号为 -1，然后向左依次是：-2,-3,...，依次类推下来。这对字符串、列表等各种序列类型都是用。
'o'
>>> str_1[-1:-3]
''
>>> str_1[-3:-1]
'.i'
>>> list_1[-3:-1]
['2', 3]
>>> #序列的切片，一定要左边的数字小有右边的数字，lang[-1:-3]就没有遵守这个规则，返回的是一个空
>>> #反转
>>> list_2=[1,2,3,4,5]
>>> list_2[::-1]  #反转
[5, 4, 3, 2, 1]
>>> list_2
[1, 2, 3, 4, 5]
>>> str_2="Python"
>>> str_2[::-1]
'nohtyP'
>>> str_2
'Python'
>>> list(reversed(list_2))
[5, 4, 3, 2, 1]
>>> #list的另外一种反转方法
>>> help(reversed)
Help on class reversed in module builtins:

class reversed(object)
 |  reversed(sequence, /)
 |  
 |  Return a reverse iterator over the values of the given sequence.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __length_hint__(...)
 |      Private method returning an estimate of len(list(it)).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __setstate__(...)
 |      Set state information for unpickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> list_2
[1, 2, 3, 4, 5]
>>> list(reversed("abcde"))
['e', 'd', 'c', 'b', 'a']
>>> len(list_2)
5
>>> list_1+list_2
['2', 3, 'lemon', 1, 2, 3, 4, 5]
>>> list_1*3
['2', 3, 'lemon', '2', 3, 'lemon', '2', 3, 'lemon']
>>> "2" in list_1
True
>>> "5" in list_1
False
>>> max(list_1)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    max(list_1)
TypeError: '>' not supported between instances of 'int' and 'str'
>>> max(list_2)
5
>>> min(list_2)
1
>>> #按照字符在 ascii 编码中所对应的数字进行比较的
>>> #比较方法略，可见前面字符串
>>> list_1.append("apple")   #向list_1中添加str类型"apple"
>>> list_1
['2', 3, 'lemon', 'apple']
>>> list_1.append(2020)
>>> list_1
['2', 3, 'lemon', 'apple', 2020]
>>> list_1[len(list_1):]=[banala]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list_1[len(list_1):]=[banala]
NameError: name 'banala' is not defined
>>> list_1[len(list_1):]=["banala"]
>>> list_1
['2', 3, 'lemon', 'apple', 2020, 'banala']
>>> 