Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> True
True
>>> False
False
>>> 2==2
True
>>> 2>=0
True
>>> 2<=3
True
>>> 2<3
True
>>> 2>3
False
>>> 34 != 34
False
>>> 34 == 34
True
>>> (4 < 5) and (5 < 6)
True
>>>  (4 < 5) and (9 < 6)
...  
SyntaxError: unexpected indent
>>> (4 < 5) and (9 < 6)
False
>>> (1>=4) or (3>2)
True
