#0x0A. Python Inheritance
Concepts reviewed:
What is a superclass, baseclass or parentclass
What is a subclass
How to list all attributes and methods of a class or instance
When can an instance have new attributes
How to inherit class from another
How to define a class with multiple base classes
What is the default class every class inherit from
How to override a method or attribute inherited from the base class
Which attributes or methods are available by heritage to subclasses
What is the purpose of inheritance
What are, when and how to use isinstance, issubclass, type and super built-in functionsPython - More Classes and Objects

## Installation

All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

```bash
./main.py
```

## Usage

Educational purposes

## Tasks
0. -lookup.py: Write a function that returns the list of available attributes and methods of an object
1. -my_list.py: Write a class MyList that inherits from list
2. -is_same_class.py:Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
3. -is_kind_of_class.py: Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
4. -inherits_from.py: Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
5. -base_geometry.py: Write an empty class BaseGeometry.
6. -base_geometry: Write a class BaseGeometry (based on 5-base_geometry.py), that raises an Exception with the message area() is not implemented
7. -base_geometry.py: Write a class BaseGeometry (based on 6-base_geometry.py). That validates value
8. -rectangle.py: Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
9. -rectangle.py: Write a class Rectangle that inherits from BaseGeometry (8-base_geometry.py).The area() method must be implemented
10. -square.py: Write a class Square that inherits from Rectangle (9-rectangle.py)
11. square.py: Write a class Square that inherits from Rectangle (10-rectangle.py): print() should print, and str() should return, the square description: [Square] <width>/<height>
