# 0x0A. Python - Inheritance

## Resources:books:
Read or watch:
* [Inheritance](https://intranet.hbtn.io/rltoken/E2Bs3bxX8GuSEKuWqswU7g)
* [Multiple inheritance](https://intranet.hbtn.io/rltoken/auwnZOKkBZ97JaLtrMryuA)
* [Inheritance in Python](https://intranet.hbtn.io/rltoken/ycewwwPmDpXqRp2R1FW51w)
* [Learn to Program 10 : Inheritance Magic Methods](https://intranet.hbtn.io/rltoken/F8LUzmvPI4yur1Z37ZM1fQ)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Why Python programming is awesome 
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes 
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions

---

### [0. Lookup](./0-lookup.py)
* Write a function that returns the list of available attributes and methods of an ob
>$ ./0-main.py

>      ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>
>       ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
>
>       ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>
>vagrant@file$

### [1. My list](./1-my_list.py)
* Write a class MyList that inherits from list:
>vagrant@file$./1-main.py
>
>     [1, 4, 2, 3, 5]
>     [1, 2, 3, 4, 5]
>     [1, 4, 2, 3, 5]
>vagrant@file$
### [2. Exact same object](./2-is_same_class.py)
* Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
>vagrant@file$./2-main.py
>
>1 is an instance of the class int
>
>vagrant@file$
### [3. Same class or inherit from](./3-is_kind_of_class.py)
* Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
>vagrant@file$./3-main.py
>
>1 comes from int
>
>1 comes from object
>
>vagrant@file$
### [4. Only sub class of](./4-inherits_from.py)
* Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
>vagrant@file$/4-main.py
>
>True inherited from class int
>
>True inherited from class object
>
>vagrant@file$
### [5. Geometry module](./5-base_geometry.py)
* Write an empty class BaseGeometry.
>vagrant@file$./5-main.py
>
><5-base_geometry.BaseGeometry object at 0x7f2050c69208>
>
>['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>
>['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>
>vagrant@file$
### [6. Improve Geometry](./6-base_geometry.py)
* Write a class BaseGeometry (based on 5-base_geometry.py).
  *Public instance method: def area(self): that raises an Exception with the message area() is not implemented
  *You are not allowed to import any module
>vagrant@file$./6-main.py
>
>[Exception] area() is not implemented
>
>vagrant@file$
### [7. Integer validator](./7-base_geometry.py)
* Write a class BaseGeometry (based on 6-base_geometry.py).
  ***Public instance method: def area(self): that raises an Exception with the message area() is not implemented
  ***Public instance method: def integer_validator(self, name, value): that validates value
	  1.you can assume name is always a string
>vagrant@file$./7-main.py
>
>[TypeError] name must be an integer
>
>[ValueError] age must be greater than 0
>
>[ValueError] distance must be greater than 0
>
>vagrant@file$
### [8. Rectangle](./8-rectangle.py)
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
  ***Instantiation with width and height: def __init__(self, width, height):
>vagrant@file$./8-main.py
><8-rectangle.Rectangle object at 0x7f6f488f7eb8>
>
>['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
>
>[AttributeError] 'Rectangle' object has no attribute 'width'
>
>[TypeError] height must be an integer
>
>vagrant@file$
### [9. Full rectangle](./9-rectangle.py)
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
	***Instantiation with width and height: def __init__(self, width, height):
>vagrant@file$./9-main.py
>
>[Rectangle] 3/5
>15
>
>
>vagrant@file$
### [10. Square #1](./10-square.py)
* Write a class Square that inherits from Rectangle (9-rectangle.py):
>vagrant@file$./10-main.py
>
>[Rectangle] 13/13
>
>169
>
>vagrant@file$
### [11. Square #2](./11-square.py)
* Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
>vagrant@file$
>vagrant@file$

---

## Author
* **Camilo Barreiro** - [CBarreiro96](https://github.com/CBarreiro96?tab=repositories)
