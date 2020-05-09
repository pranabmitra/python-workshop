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