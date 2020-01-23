#0x0B. Python - Input/Output.
Concepts reviewed.
-Import
-Exceptions
-Class
-Private attribute
-Getter/Setter
-Class method
-Static method
-Inheritance
-Unittest
-Read/Write file
-What is Unit testing and how to implement it in a large project
-How to serialize and deserialize a Class
-How to write and read a JSON file
-/*What is *args and how to use it
-What is **kwargs and how to use it
-How to handle named arguments in a function

## Installation

All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

```bash
./main.py
```

## Usage

Educational purposes

## Tasks
0. -tests/(This folder will have all unittests for the project)
1. -Create the class Base: private class attribute __nb_objects = 0, class constructor: def __init__(self, id=None).
2. -Write the class Rectangle that inherits from Base: __width -> width, __height -> height, __x -> x, __y -> y
3. Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).
4. Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
5. -Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you dont need to handle x and y here.
6. -Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
7. -Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
8. -Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.
9- Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.
10. -Write the class Square that inherits from Rectangle
11. -Update the class Square by adding the public getter and setter size
12. -Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.
13. Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.
14. Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.
15. Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:
16. -Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs
17. -Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string
18. -Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.
19. -Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.
