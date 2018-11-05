Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "hello"
>>> str2 = 'there'
>>> bob = str1 + str2
>>> print(bob)
hellothere
>>> str'123'
SyntaxError: invalid syntax
>>> str3 = '123'
>>> str3 = str3 +1

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str3 = str3 +1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x = int(str3) + 1
>>> print(x)
124
>>> name = input('enter:')
enter:chuck

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name = input('enter:')
  File "<string>", line 1, in <module>
NameError: name 'chuck' is not defined
>>> name = raw_input('enter:')
enter:chuck
>>> print(name)
chuck
>>> apple = raw_input('enter:')
enter:100
>>> x = apple - 10

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x = apple - 10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple) - 10
>>> print(x)
90
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
>>> zot = 'abc'
>>> print(zot[5])

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> fruit = 'banana'
>>> print(len(fruit))
6
>>> fruit = 'banana'
>>> x = len(fruit)
>>> print(x)
6
>>> fruit = 'banana'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> 
>>> 
================== RESTART: /home/user/RTR105/test_05_11.py ==================
b
a
n
a
n
a
>>> 
================== RESTART: /home/user/RTR105/test_05_11.py ==================
b
a
n
a
n
a
b
a
n
a
n
a
>>> 
================== RESTART: /home/user/RTR105/test_05_11.py ==================
1
2
3
>>> ls - l

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ls - l
NameError: name 'ls' is not defined
>>> s = 'monty python'
>>> print(s[0:4])
mont
>>> print(s[6:7])
p
>>> print(s[6;20])
SyntaxError: invalid syntax
>>> print(s[6:20])
python
>>> print(s[8:])
thon
>>> a = 'hello'
>>> b = a + 'there'
>>> print(b)
hellothere
>>> c = a + '' + 'there'
>>> print(c)
hellothere
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
	print(found it!)
	
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>>  if 'a' in fruit:
	 
  File "<pyshell#55>", line 1
    if 'a' in fruit:
    ^
IndentationError: unexpected indent
>>> if 'a' in fruit:
	print('found it!')

	
found it!
>>> if word == 'banana':
	print('all right, bananas.')

	
all right, bananas.
>>> 
================== RESTART: /home/user/RTR105/test_05_11.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/test_05_11.py", line 31, in <module>
    if word < 'banana':
NameError: name 'word' is not defined
>>> 
================== RESTART: /home/user/RTR105/test_05_11.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/test_05_11.py", line 31, in <module>
    if word < 'banana':
NameError: name 'word' is not defined
>>> greet = 'Hello Bob'
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> fruit = 'banana'
>>> pos = fruit.find('na')
>>> print(pos)
2
>>> aa = fruit.find('z')
>>> print(aa)
-1
>>> greet = 'Hello Bob'
>>> nnn = greet.upper()
>>> print(nnn)
HELLO BOB
>>> www = greet.lower()
>>> print(www)
hello bob
>>> greet = 'Hello Bob'
>>> nstr = greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr = greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> 
