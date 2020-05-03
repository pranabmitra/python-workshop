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

###### Iterative and Recursive functions
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
```


