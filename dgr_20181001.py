Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> a = 10
>>> a
10
>>> a = a
>>> a + a
20
>>> b = 13.29
>>> a + b
23.29
>>> c = P

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c = P
NameError: name 'P' is not defined
>>> c = 'P'
>>> c
'P'
>>> 
