### Programs


###### Script
We've created a `my_script.py` file. To run the script, we have to run the below command:
```python
python my_script.py
```

###### Module
We've created a `my_module.py` file. To use this module from other place, we can follow the below commands:
```python
from my_module import compute
compute([5, 7])
```

Since we've added a docstring, we can use the `help` method to the details of the module:
```python
import my_module
help(my_module)

# or
my_module.__doc__ # print the docstring
```

###### Sample Program
```python
"""
Binary Search Program
"""
data = [2, 4, 5, 8, 14, 15, 18]
target = 14

left = 0
right = len(data) - 1
index = -1

while (left <= right):
    mid = left + (right - left) // 2
    if (data[mid] == target):
        index = mid
        break
    elif (data[mid] > target):
        right = mid - 1
    else:
        left = mid + 1
     
print(index) # 4
```

###### Functions
A function is a reusable piece of code that is only run when it is called.

```python
def add(a, b):
    return a + b

add(32, 45) # 77

# With default value
def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

print(convert_usd_to_aud(100))
print(convert_usd_to_aud(100, .78))
# First one is Positional arguments
# Second one is Keywordarguments
print(convert_usd_to_aud(100, rate=.78))
```

###### Iterative and Recursive Functions
_Factorial program:_
```python
# Iterative way
def fibonacci_recursion(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)

print(factorial_iterative(6)) # 720

# Recursive way
def factorial_recursion(n):
    if n == 1:
        return 1
    
    return n * factorial_recursion(n - 1)

print(factorial_recursion(6)) # 720
```

_Fibonacci program:_
```python
# Iterative way
def fibonacci_iterative(n):
    a = 0
    b = 1
    count = 1
    while count < n:
        a, b = b, a + b
        count += 1
        
    return b

# Recursive way
def fibonacci_recursion(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)

# Using Dynamic Programming, stored the previous value
storage = { 0: 0, 1: 1 }
def fibonacci_dynamic(n):
    if n in storage:
        return storage[n]
    else:
        storage[n] = fibonacci_dynamic(n - 2) + fibonacci_dynamic(n - 1)
        return storage[n]
        
print(fibonacci_dynamic(100)) # 354224848179261915075
```

###### Variable scope
```python
# Local scope
x = 3
def my_func():
    x = 5
    print(x) # 5
my_func()
print(x) # 3

# Global scope
"""
To use the existing globally defined variable
"""
x = 3
def my_func():
    global x
    x = 5
    print(x) # 5
my_func()
print(x) # 5

# Nonlocal scope
"""
It looks "one level up" in the code
"""
x = 4
def myfunc():
    x = 3
    def inner():
        nonlocal x
        print(x) # 3
    inner()
myfunc()
print(x) # 4
```

##### Lambda Functions
Lambda functions are small, anonymous functions that can be defined in a simple one-line syntax:
```python
lambda arguments : expression
```

```python
add = lambda x, y: x + y
print(add(2, 5)) # 7

# map
nums = [-3, 1, 4, 7]
result = map(lambda x: x * 2, nums)
print(list(result)) # [-6, 2, 8, 14]

# filter
"""
Print all even numbers upto 10
"""
nums = list(range(11))
filtered = filter(lambda x: x % 2 == 0, nums)
list(filtered) # [0, 2, 4, 6, 8, 10]
```


