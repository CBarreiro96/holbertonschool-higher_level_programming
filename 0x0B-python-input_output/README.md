# 0x0B. Python - Input/Output

## Resources:books:
Read or watch:
* [7.2. Reading and Writing Files](https://intranet.hbtn.io/rltoken/c5ypFfQwcM-SZ-7tr3WuxA)
* [8.7. Predefined Clean-up Actions](https://intranet.hbtn.io/rltoken/1wqMFejKqBva-Lxws0lftw)
* [Dive Into Python 3: Chapter 11. Files](https://intranet.hbtn.io/rltoken/8aSPOpBZj9B1DB6GfoEWfg)
* [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/XBqM3BrA_rUBw6DXw4X98Q)
* [Learn to Program 8 : Reading / Writing Files](https://intranet.hbtn.io/rltoken/derf9VLFVDnSgX2n-drwnw)
* [Automate the Boring Stuff with Python](https://intranet.hbtn.io/rltoken/Y77h8aeRoljlN643yKfdTg)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file 
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string 
* How to convert a JSON string to a Python data structure

---

### [0. Read file](./0-read_file.py)
* Write a function that reads a text file (UTF8) and prints it to stdout:


### [1. Number of lines](./1-number_of_lines.py)
* Write a function that returns the number of lines of a text file:


### [2. Read n lines](./2-read_lines.py)
* Write a function that reads n lines of a text file (UTF8) and prints it to stdout:


### [3. Write to a file](./3-write_file.py)
* Write a function that writes a string to a text file (UTF8) and returns the number of characters written:


### [4. Append to a file](./4-append_write.py)
* Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:


### [5. To JSON string](./5-to_json_string.py)
* Write a function that returns the JSON representation of an object (string):
>valgrand@file$./5-main.py
>
>[1, 2, 3]
>
><class 'str'>
>
>{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
>
><class 'str'>
>
>[TypeError] {3, 132} is not JSON serializable
>
>valgrand@file$
### [6. From JSON string to Object](./6-from_json_string.py)
* Write a function that returns an object (Python data structure) represented by a JSON string:
>valgrand@file$./6-main.py
>
>[1, 2, 3]
>
><class 'list'>
>
>{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
>
><class 'dict'>
>
>[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
>
>valgrand@file$
### [7. Save Object to a file](./7-save_to_json_file.py)
* Write a function that writes an Object to a text file, using a JSON representation:
>valgrand@file$./7-main.py
>
>[TypeError] {3, 132} is not JSON serializable
>
>valgrand@file$
### [8. Create object from a JSON file](./8-load_from_json_file.py)
* Write a function that creates an Object from a “JSON file”:
>valgrand@file$./8-main.py
>
>[1, 2, 3]
>
><class 'list'>
>
>{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
>
><class 'dict'>
>
>[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
>
>[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
>
>valgrand@file$
### [9. Load, add, save](./9-add_item.py)
* Write a script that adds all arguments to a Python list, and then save them to a file:
>valgrand@file$./9-add_item.py Holberton School
>
>["Holberton", "School"]
>
>valgrand@file$
### [10. Class to JSON](./10-class_to_json.py)
* Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
>valgrand@file$./10-main.py
>
><class '10-my_class.MyClass'>
>
>[MyClass] John - 89
>
><class 'dict'>
>
>{'name': 'John', 'number': 89}
>
>valgrand@file$./10-main_2.py
>
><class '10-my_class_2.MyClass'>
>
>MyClass] John - 4 => 1
>
>class 'dict'>
>
>'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
>
>valgrand@file$
### [11. Student to JSON](./11-student.py)
* Write a class Student that defines a student by:
>valgrand@file$./11-main.py
>
><class 'dict'>
>
>ohn
>
>class 'str'>
>
>23
<
><class 'int'>
>
><class 'dict'>
>
>Bob
>
><class 'str'>
<
>27
>
><class 'int'>
>
>11
>
>valgrand@file$
### [12. Student to JSON with filter](./12-student.py)
* Write a class Student that defines a student by: (based on 11-student.py)
>valgrand@file$./12-main.py
>
>{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
>
>{'age': 27, 'first_name': 'Bob'}
>
>{'age': 27}
>
>valgrand@file$
### [13. Student to disk and reload](./13-student.py)
* Write a class Student that defines a student by: (based on 12-student.py)
>valgrand@file$
>valgrand@file$
### [14. Pascal's Triangle](./14-pascal_triangle.py)
* Technical interview preparation: 
>valgrand@file$
>valgrand@file$

---

## Author
* **Camilo Barreiro** - [CBarreiro96](https://github.com/CBarreiro96?tab=repositories)
