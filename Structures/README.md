#### Data Structures

There are four types of data structures in Python: __list__, __tuple__, __set__ and __dictionary__.

| Data Types | Description            | Example     |
| ---------- | ---------------------- | ----------  |
| List       | A collection which is ordered and changeable. It allows duplicate members.      | list = ["one", "two", "three"]   |
| Tuple      | A collection which is ordered and unchangeable. It allows duplicate members.     | tuple = ("one", "two", "three")   | 
| Set        | A collection which is unordered and unindexed. No duplicate members.      | set = {"apple", "banana", "cherry"}  | 
| Dictionary | A collection which is unordered, changeable and indexed. No duplicate members. |    dict = { "name": "X", "year": "2000" } |

#### List
```python
list = [1, 2, 3]
print(len(list)) # 3
list[0:2] # [1, 2]
list.append(4)
print(list) # [1, 2, 3, 4]
list.remove(2) # [1, 3, 4]
list.insert(1, 5)] # [1, 5, 3, 4]

# concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2) # [1, 2, 3, 4, 5, 6]

# Nested List
m = [[1, 2, 3], [4, 5, 6]]
print(m[1][1]) # 5
print(m[1][-1]) # 6

# Print all elements
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j])

# or
for row in m:
    for col in row:
        print(col)

# Zip - combine lists
fruit = ['banana', 'strawberry']
count = [2, 3]
basket = zip (fruit, count)
print(list(basket)) # [('banana', 2), ('strawberry', 3)]
```

#### Tuple
```python
lang = ('English', 'Bangla')
len(lang) # 2

newTuple = lang + ('German', 'Spanish')
newTuple # ('English', 'Bangla', 'German', 'Spanish')
print(newTuple[1]) # Bangla
```

#### Set
```python
s = set([1, 2, 2, 3, 3, 3, 4, 5, 6])
# unordered collections of unique and immutable objects
print(s) # {1, 2, 3, 4, 5, 6}
s.add(7) # {1, 2, 3, 4, 5, 6, 7}
s.remove(6) # {1, 2, 3, 4, 5, 7}

# Union
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2 | { 7 }) # {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6}

# Intersection
print(s1 & s2) # {3, 4}
print(s1.intersection(s2)) # {3, 4}

# Difference
print(s1 - s2) # {1, 2}
print(s1.difference(s2)) # {1, 2}

# Subset
s3 = {1, 2, 3}
s4 = {1, 2, 3, 4, 5}
print(s3 < s4) # True
print(s3.issubset(s4)) # True
# Identical; A set is not a subset of itself
print(s3 < s3) # False

# Superset
s3 = {1, 2, 3}
s4 = {1, 2, 3, 4, 5}
print(s4 > s3) # True
print(s4.issuperset(s3)) # True
# Identical; A set is not a superset of itself
print(s3 > s3) # False
```

#### Dictionary
```python
# Example
user = {
    "name": "John Snow",
    # store a list inside the dict
    "interests": ["Programming", "Travel", "Music"], 
    "department": "Software Development"
}

user['name'] # 'John Snow'
type(user) # dict
type(user["interests"]) # list
tuple(user.keys()) # ('name', 'interests', 'department')
tuple(user.values())
list(user.items()) # output below
"""
[('name', 'John Snow'),
 ('interests', ['Programming', 'Travel', 'Music']),
 ('department', 'Software Development')]
"""
```