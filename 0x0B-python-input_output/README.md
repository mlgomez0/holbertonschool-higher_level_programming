#0x0B. Python - Input/Output.
Concepts reviewed.
-How to open a file
-How to write text in a file
-How to read the full content of a file
-How to read a file line by line
-How to move the cursor in a file
-How to make sure a file is closed after using it
-What is and how to use the with statement
-What is JSON
-What is serialization
-What is deserialization
-How to convert a Python data structure to a JSON string
-How to convert a JSON string to a Python data structure

## Installation

All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

```bash
./main.py
```

## Usage

Educational purposes

## Tasks
0. -read_file.py: Write a function that reads a text file (UTF8) and prints it to stdout:
1. -number_of_lines.py: Write a function that returns the number of lines of a text file:
2. -read_lines.py: Write a function that reads n lines of a text file (UTF8) and prints it to stdout:
3. -write_file.py: Write a function that writes a string to a text file (UTF8) and returns the number of characters written:.
4. -append_write.py: Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
5. -to_json_string.py: Write a function that returns the JSON representation of an object (string):
6. -from_json_string.py: Write a function that returns an object (Python data structure) represented by a JSON string:
7. -save_to_json_file.py: Write a function that writes an Object to a text file, using a JSON representation:
8. -load_from_json_file.py: Write a function that creates an Object from a “JSON file”:
9. -add_items.py: Write a script that adds all arguments to a Python list, and then save them to a file:
10. -class_to_json.py: Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
11. -student.py: Write a class Student
12. -student.py: Write a class Student that defines a student by: (based on 11-student.py)- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
13. -student.py: Write a class Student that defines a student by: (based on 12-student.py)- Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
14. -pascal_triangle.py: Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
