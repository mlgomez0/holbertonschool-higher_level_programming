#0x13. Javascript - Objects, Scopes and Closures

## Concepts

- How to create an object in Javascript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Usage

Educational purposes

## Tasks

0. 0-rectangle.js : Empty class Rectangle that defines a rectangle.
1. 1-rectangle.js : class Rectangle that defines a rectangle (constructor must take 2 arguments w and h, Initialize the instance attribute width with the value of w, Initialize the instance attribute height with the value of h)
2. 2-rectangle.js: Same as previous + If w or h is equal to 0 or not a positive integer, create an empty object).
3. 3-rectangle.js: Same as previous + Create an instance method called print() that prints the rectangle using the character X.
4. 4-rectangle.js: Same as previous + Create an instance method called rotate() that exchanges the width and the height of the rectangle, Create an instance method called double() that multiples the width and the height of the rectangle by 2.
5. 5-square.js: class Square that defines a square and inherits from Rectangle of 4-rectangle.js
- The constructor must take 1 argument: size
- he constructor of Rectangle must be called (by using super())
6. 6-square.js: class Square that defines a square and inherits from Square of 5-square.js.
- Create an instance method called charPrint(c) that prints the rectangle using the character c (If c is undefined, use the character X)
7. 7-occurrences.js: function that returns the number of occurrences in a list.
- Prototype: exports.nbOccurences = function (list, searchElement)
8. 8-esrever.js: function that returns the reversed version of a list.
- not allow to use the built-in method reverse
-Prototype: exports.esrever = function (list).
9. 9-logme.js: function that prints the number of arguments already printed and the new argument value:
- Prototype: exports.logMe = function (item)
- Output format: <number arguments already printed>: <current argument value>
10. 10-converter.js: function that converts a number from base 10 to another base passed as argument:
- Prototype: exports.converter = function (base)
- Import is not allowed
- It is not allowed to declare any new variable (var, let, etc..).
