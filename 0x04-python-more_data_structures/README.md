# 0x04. Python - More Data Structures: Set, Dictionary

## Resources:books:
Read or watch:
* [Data structures](https://intranet.hbtn.io/rltoken/dnFegYagqFoW7WraIP-9RA)
* [Lambda, filter, reduce and map](https://intranet.hbtn.io/rltoken/xXAlsMIs9-sCL4fljYeNfg)
* [Learn to Program 12 Lambda Map Filter Reduce](https://intranet.hbtn.io/rltoken/AT-UtsGuhgIzQSwSdKvckw)

<details>
<summary> <b>🛠⚙️ Command ⚙️🛠</b> </summary>
<div align="center">
<table>
    <tr>
        <td align="center"><b>Concept</b></td>
        <td align="center"><b>Description</b></td>
        <td align="center" colspan="2"><b>Example</b></td>
    </tr>
    <tr>
        <td align="center" rowspan="8">SETS</td>
        <td align="center" rowspan="8">It is a data structure that mathematical sets represent</td>
        <td align="center"><b>Set creation</b></td>
                <td align="center">
            <h4>No empty code</h4>
            <h6>INPUT</h6>
            <code>
                my_set = {5, 8, 2, 9, 4}
            </code>
            <br>
            <code>
                print(my_set)
            </code>
            <h6>OUTPUT</h6>
            <code>
                {2, 4, 5, 8, 9}
            </code>
            <h4>Empty code</h4>
            <h6>INPUT</h6>
            <code>
                my_set = set()<br>
            </code>
            <br>
            <code>
                print(my_set)
            </code>
            <h6>OUTPUT</h6>
            <code>
                set()
            </code>
        </td>
    </tr>
    <tr>
        <td align="center" rowspan="6"><b>Set operation</b></td>
        <td align="center"><b>I. Contention</b></td>
    </tr>
    <tr>
        <td align="center">
            <h6>INPUT</h6>
            <code>
                my_set = {'S', 'E', 'T'}
            </code>
            <br>
            <code>
                print('S' in my_set)
            </code>
            <h6>OUTPUT</h6>
            <code>
                True
            </code>
        </td>
    </tr>
    <tr>
        <td align="center"><b>II UNION </b></td>
    </tr>
    <tr>
        <td align="center">
            <h6>INPUT</h6>
            <code>
                set_1 = {1, 2, 3}
            </code>
            <br>
            <code>
                set_2 = {2, 4, 6}
            </code>
            <br>
            <code>
               union_set = set_1.union(set_2) 
            </code>
            <br>
            <code>
                print(union_set)
            </code>
            <h6>OUTPUT</h6>
            <code>
                {1, 2, 3, 4, 6}
            </code>
        </td>
    </tr>
    <tr>
        <td align="center"><b>III INTERSECTION</b><td>
    </tr>
    <tr>
        <td align="center">
            <h6>INPUT</H6>
            <code>
                set_1 = {1, 2, 3}
            </code>
            <br>
            <code>
            set_2 = {1, 3, 5}
            </code>
            <br>
            <code>
            intersection_set = set_1.intersection(set_2)
            </code>
            <br>
            <code>
            print(intersection_set)
            </code>
            <h6>OUTPUT</h6>
            <code>
            {1, 3}
            </code>
        </td>
    </tr>
</table>
</div>
</details>

---

## Learning Objectives:bulb:
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What are set and how to use them
* What are the most common methods of set and how to use them
* When to use sets versus lists
* How to iterate into a set
* What are dictionary and how to use them
* When to use dictionaries versus lists or sets
* What is a key in a dictionary
* How to iterate into a dictionary
* What is a lambda function
* What is map, reduce and map functions

---

### [0. Squared simple](./0-square_matrix_simple.py)
* Write a function that computes the square value of all integers of a matrix.


### [1. Search and replace](./1-search_replace.py)
* Write a function that replaces all occurrences of an element by another in a new list.


### [2. Unique addition](./2-uniq_add.py)
* Write a function that adds all unique integers in a list (only once for each integer).


### [3. Present in both](./3-common_elements.py)
* Write a function that returns a set of common elements in two sets.


### [4. Only differents](./4-only_diff_elements.py)
* Write a function that returns a set of all elements present in only one set.


### [5. Number of keys](./5-number_keys.py)
* Write a function that returns the number of keys in a dictionary.


### [6. Print sorted dictionary](./6-print_sorted_dictionary.py)
* Write a function that prints a dictionary by ordered keys.


### [7. Update dictionary](./7-update_dictionary.py)
* Write a function that replaces or adds key/value in a dictionary.


### [8. Simple delete by key](./8-simple_delete.py)
* Write a function that deletes a key in a dictionary.


### [9. Multiply by 2](./9-multiply_by_2.py)
* Write a function that returns a new dictionary with all values multiplied by 2


### [10. Best score](./10-best_score.py)
* Write a function that returns a key with the biggest integer value.


### [11. Multiply by using map](./11-multiply_list_map.py)
* Write a function that returns a list with all values multiplied by a number without using any loops.


### [12. Roman to Integer](./12-roman_to_int.py)
* Technical interview preparation: 


### [13. Weighted average!](./100-weight_average.py)
* Write a function that returns the weighted average of all integers tuple (<score>, <weight>)


### [14. Squared by using map](./101-square_matrix_map.py)
* Write a function that computes the square value of all integers of a matrix using map


### [15. Delete by value](./102-complex_delete.py)
* Write a function that deletes keys with a specific value in a dictionary.


### [16. CPython #1: PyBytesObject](./103-python.c)
* Create two C functions that print some basic info about Python lists and Python bytes objects.



Python lists:

---

## Author
* **Camilo Barreiro** - [CBarreiro96](https://github.com/CBarreiro96?tab=repositories)