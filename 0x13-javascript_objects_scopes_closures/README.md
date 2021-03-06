<div align="center"><img src="https://user-images.githubusercontent.com/66263776/98416555-43fa9b80-204d-11eb-800a-df8e19b62655.jpg" width="500" height= "200"> </div>

# <img src="https://user-images.githubusercontent.com/66263776/98705433-b6b88f00-234b-11eb-97b7-cb193f7424f4.png" width="20" height= "30">  0x13. Javascript - Objects, Scopes and Closures <img src="https://user-images.githubusercontent.com/66263776/98705433-b6b88f00-234b-11eb-97b7-cb193f7424f4.png" width="20" height= "30">

## :book: Description of the proyect :book:
In this proyect we are going to do diferent task about Javascrpt language, in this repo you ar going to learn about Object, inherente, classes, initialize instance with **this**, ocurrence  and thing like that

## :books: Important concept :books:
In this project you need to know some concept about Object, Classs inherence, clouser etc <br>
In the next link you ar going to find a resume about this concept:
<details>
	<summary>:boom:<b>How to create an object in Javascript.</b></summary>
	<br/>
    An object is a collection of related data and/or functionality (which usually consists of several variables and functions — which are called properties and methods when they are inside objects.) Let's work through an example to understand what they look like.

As with many things in JavaScript, creating an object often begins with defining and initializing a variable. <br>
**For example:**

```javascript
    const objectName = {
    member1Name: member1Value,
    member2Name: member2Value,
    member3Name: member3Value
    };
```
</details>
<details>
	<summary>:boom:<b>How to declare a class. </b></summary>
	<br/>
    One way to define a class is using a class declaration. To declare a class, you use the class keyword with the name of the class ("Rectangle" here).

```javascript
    class Rectangle {
        constructor(height, width) {
            this.height = height;
            this.width = width;
        }
    }
```

</details>
<details>
	<summary>:boom:<b>What "THIS" mean. </b></summary>
	<br/>
    this keyword refers to an object, that object which is executing the current bit of javascript code. In other words, every javascript function while executing has a reference to its current execution context, called this. Execution context means here is how the function is called.
</details>
<details>
	<summary>:boom:<b>Importance of Scope</b></summary>
	<br/>

The scope is a policy that manages the availability of variables. A variable defined inside a scope is accessible only within that scope, but inaccessible outside.<br>
In JavaScript, scopes are created by code blocks, functions, modules.<br>
While const and let variables are scoped by code blocks, functions or modules, var variables are scoped only by functions or modules.<br>
Scopes can be nested. Inside an inner scope you can access the variables of an outer scope.<br>
The lexical scope consists of the outer function scopes determined statically. Any function, no matter the place where being executed, can access the variables of its lexical scope (this is the concept of closure).
</details>
<details>
	<summary>:boom:<b>What is clousure</b></summary>
	<br/>
    Closure means that an inner function always has access to the vars and parameters of its outer function, even after the outer function has returned.<br>
    <b>Example:</b>

```javascript
    function OuterFunction() {

        var outerVariable = 1;//---> Lexical Scope

        function InnerFunction() {
            alert(outerVariable); //----> Capture variable  of outerVariable
        }

        InnerFunction();
    }
```
</details>
<details>
	<summary>:boom: <b>What is a prototype</b></summary>
	<br/>

The prototype is an object that is associated with every functions and objects by default in JavaScript, where function's prototype property is accessible and modifiable and object's prototype property (aka attribute) is not visible.

Every function includes prototype object by default. 

```javascript
    function Student() {
        this.name = 'John';
        this.gender = 'M';
    }

    Student.prototype.age = 15;

    var studObj1 = new Student();
    alert(studObj1.age); // 15

    var studObj2 = new Student();
    alert(studObj2.age); // 15
```
</details>

<br>

If you like to know about this you can visit the follow page:
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* 
## :memo: Activities :memo:

### [Rectangle #0]() 

Write an empty class Rectangle that defines a rectangle:

* You must use the class notation for defining your class
```javascript
user@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

user@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Function: Rectangle]
user@ubuntu:~/0x13$ 
```


### [Rectangle #1]() 

Write a class Rectangle that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h

```javascript
user@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

user@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
user@ubuntu:~/0x13$ 
```


    
    
    


### [Rectangle #2]() 

Write a class Rectangle that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object

```javascript
user@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

user@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
user@ubuntu:~/0x13$ 
```


### [Rectangle #3]() 

Write a class Rectangle that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments: w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called print() that prints the rectangle using the character X

```javascript
user@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

user@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
user@ubuntu:~/0x13$ 
```


### [Rectangle #4]() 

Write a class Rectangle that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments: w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called print() that prints the rectangle using the character X
* Create an instance method called rotate() that exchanges the width and the height of the rectangle
* Create an instance method called double() that multiples the width and the height of the rectangle by 2

```javascript
user@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

user@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
user@ubuntu:~/0x13$ 
```

### [Square #0]() 

Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

* You must use the class notation for defining your class and extends
* The constructor must take 1 argument: size
* The constructor of Rectangle must be called (by using super())

```javascript
user@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

user@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
user@ubuntu:~/0x13$ 
```



### [Square #1 ]()

Write a class Square that defines a square and inherits from Square of 5-square.js:

* You must use the class notation for defining your class and extends
* Create an instance method called charPrint(c) that prints the rectangle using the character c
    * If c is undefined, use the character X

```javascript
user@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

user@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
user@ubuntu:~/0x13$ 
```



### [Occurrences]() 

Write a function that returns the number of occurrences in a list:

* Prototype: exports.nbOccurences = function (list, searchElement)

```javascript
user@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["H", 12, "c", "H", "Holberton", 8], "H"));

user@ubuntu:~/0x13$ ./7-main.js
1
4
2
user@ubuntu:~/0x13$ 
```


### [Esrever]() 

Write a function that returns the reversed version of a list:

* Prototype: exports.esrever = function (list)
* You are not allow to use the built-in method reverse

```javascript
user@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["Holberton", 89, { id: 12 }, "String"]));

user@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'Holberton' ]
user@ubuntu:~/0x13$ 
```


### [Log me]()

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

* Prototype: exports.logMe = function (item)
* Output format: <number arguments already printed>: <current argument value>

```javascript
user@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Holberton");
logMe("School");

user@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Holberton
2: School
user@ubuntu:~/0x13$ 
```

### [Number conversion]()

Write a function that converts a number from base 10 to another base passed as argument:

* Prototype: exports.converter = function (base)
* You are not allowed to import any file
* You are not allowed to declare any new variable (var, let, etc..)

```javascript
user@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

user@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
user@ubuntu:~/0x13$ 
```