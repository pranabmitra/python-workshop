#### Standard Math Operations

| Operation           | Symbol | Example     |
| ------------------- | ------ | ----------  |
| Addition            | +      | 2 + 3 = 5   |
| Subtraction         | -      | 5 - 3 = 2   | 
| Multification       | *      | 5 * 2 = 10  | 
| Division            | /      | 5 / 2 = 2.5 |
| Integer Division    | //     | 5 // 2 = 2  |
| Exponentiation      | **     | 5 ** 2 = 25 |
| Modulus / Remainder | %      | 5 % 2 = 1   |


#### Order of Operations
___BODMAS___
According to Bodmas rule, if an expression contains brackets, we have to first solve or simplify the bracket followed by of (powers and roots etc.), then division, multiplication, addition and subtraction from left to right.

```python
5 + 2 * -3          = -1
(5 + 2) * -3        = -21
(100 - 5 ** 3) / 5  = -5.0
6 + 15 % 4          = 9
2 ** 2 + 24 // 4    = 10
```

#### Types
```python
type(4)      = int
type(4.0)    = float
type('5')    = str
type(True)   = bool
int(4.99999) = 4
float(4)     = 4.0

# Changing Types
x = 10 # type(x) = int
x = x - 4.0 # type(x) = fload
```

#### Multiple Variables
```python
x, y = 9, 5
# x = 9, y = 4
```

#### Comment and Docstring
```python
# This is a comment
"""
This document determines why comments are usefull while reading and writing code
"""
```

#### String
```python
# string concatenation
a = 'Hello'
print(a + ' world') # Hello world
print(a * 4) # HelloHelloHelloHello

# String Interpolation
country = 'Japan'
capital = 'Tokyo'
# 1. Comma separators
print(capital, 'is the capital of', country)
# 2. Format
print('{} is the capital of {}'.format(capital, country))
# Output: Tokyo is the capital of Japan

a.lower() # hello
a.capitalize() # Hello
a.upper() # HELLO
# no of occurrences in the word
a.count('l') # 2

# Input
print('What is your name?')
name = input();
print('Hello, ' + name + '.')

# Indexing
greetings = 'Hello'
greetings[0] # 'H'
greetings[1] # 'e'
"""Negative numbers start at the end of the string. Start with -1 since -0 is the same as 0."""
greetings[-1] # 'o'
greetings[-5] # 'H'

# Slicing - subset of a string or other element
city = 'San Francisco'
"""The lower bound of a slice is always included, but the upper bound is not."""
city[4:8] # 'Fran'
city[0:3] # 'San'
city[8:] # 'cisco
city[:8] # 'San Fran'
city[:-3] # 'San Franci'
city[-3:] # 'sco'
```

#### Boolean
```python
# Boolean values must be capitalized in Python.
# Value can be: True or False
a, b = True, False
# Logical operators: 'and', 'or', and 'not'
a or b # True
a and b # False
not a # False

"""Python often conforms to mathematical truths, even with integer division. Since 5 and 5.0 are equivalent mathematically, they would be equivalent in Python, even though the types are different"""
5 == 5.0 # True
"""However, because of the different types, below code will return False"""
5 == '5' # False

# Compare
# Python uses alphabetical order
'a' < 'A' # False
'a' < 'c' # True
'ac' < 'ab' # False
'ac' < 'ad' # True
```

#### Conditionals
```python
# Python uses indentation instead of brackets.
age = 20
if age < 20:
    print('You are less than 20 years old.')
elif age == 20:
    print('You are now 20 years old')
else:
    print('You are above 20')
```

#### Loop
```python
x = 5
while x <= 20:
    print(x)
    x += 5

# Example: Find the GCM of 24 and 36
a, b = 24, 36
while ((b % a) != 0):
    temp = a
    a = b % a
    b = temp
    
print('GCM is:', a) # GCM is: 12

# For Loop
for i in 'Hello':
    print(i) # H, e l, l, o

for i in range(1,5):
    print(i) # 1, 2, 3, 4

for i in range(5):
    print(i) # 0, 1, 2, 3, 4

for i in range(1, 5, 2):
    print(i) # 1, 3

for i in range(3, 0, -1):
   print(i) # 3, 2, 1
```