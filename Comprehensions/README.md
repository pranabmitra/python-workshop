### Pythonic way

###### List Comprehensions
```python
# Squares of all numbers from a list.
# We can do it in a single line.
squares = [x**2 for x in [1,2,3,4,5]]
print(squares) # [1, 4, 9, 16, 25]

# Print squares only for odd nubmbers from the list
squares = [x**2 for x in range(1, 6) if x % 2 != 0]
print(squares) # [1, 9, 25]


# Multiple input lists

print([x*y for x in ['one', 'two'] for y in [1,2]])
# ['one', 'oneone', 'two', 'twotwo']
print([x*y for x in [1,2] for y in ['one', 'two']])
# ['one', 'two', 'oneone', 'twotwo']
```

###### Set Comprehensions
```python
print([a + b for a in [0, 1, 2, 3] for b in [4, 3, 2, 1]])
# [4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4, 3, 7, 6, 5, 4]

# Using Set
print({a + b for a in [0, 1, 2, 3] for b in [4, 3, 2, 1]})
# {1, 2, 3, 4, 5, 6, 7} // without duplicate entries
```

###### Dictionaly Comprehensions
```python
# Dictionaries cannot contain duplicate keys. That's why 'John' is being shown only once
names = ["John", "Eric", "Denis", 'John']
print({k:len(k) for k in names})
# {'John': 4, 'Eric': 4, 'Denis': 5}
```

###### Default Dict
```python
from collections import defaultdict

courses = defaultdict(lambda: 'No entry!') # default value for missing keys
courses['python'] = 'This is Python'
print(courses['python']) # This is Python
print(courses['java']) # No entry!
```

###### Infinite Sequences and takewhile
The `__next__()` method never raises a `StopIteration` error. That means it never exits. We can fix this by using the `takewhile` function from `itertools` module to produce a finite sequence.

```python
class Primes:
    def __init__(self):
        self.current = 2
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            current = self.current
            square_root = int(current ** 0.5)
            is_prime = True
            if square_root >= 2:
                for i in range(2, square_root + 1):
                    if current % i == 0:
                        is_prime = False
                        break
            self.current += 1
            if is_prime:
                return current

# call
import itertools

print([p for p in itertools.takewhile(lambda x: x < 100, Primes())])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Below code will make the list infinite 
itertools.cycle(['White', 'Black'])
```

###### Generators
```python
"""
Generate prime numbsers using gernerators
"""
def primes(bound):
    candidates = list(range(2,bound))
    while(len(candidates) > 0):
        yield candidates[0]
        candidates = [c for c in candidates if c % candidates[0] != 0]

# uses
print([prime for prime in primes(100)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

###### Regex
```python
# name has `X` or `x` character
names = ["Xander Harris", "Jennifer Smith", "Timothy Jones", "Amy Alexandrescu",
"Peter Price", "Weifung Xu"]
nameWithX = [name for name in names if re.search("[Xx]", name)]
print(nameWithX)
# ['Xander Harris', 'Amy Alexandrescu', 'Weifung Xu']

# Remove all digits from the text
import re

text = "2 Dogs and 3 Cats"
pattern = "[0-9]"
replacement = ""
re.sub(pattern, replacement, text)
# ' Dogs and  Cats'
```