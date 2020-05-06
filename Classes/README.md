##### Classes

```python
class Circle():
    # common property
    is_shape = True    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

# uses
obj1 = Circle(2, 'blue')
print(obj1.radius, obj1.color, obj1.is_shape) # 2 blue True

obj2 = Circle(3, 'red')
print(obj2.radius, obj2.color, obj2.is_shape) # 3 red True
```

###### Keyword Arguments
```python
class Circle():
    is_shape = True
    def __init__(self, radius, color='red', border=None):
        self.radius = radius
        self.color = color

# uses
obj = Circle(23)
obj.color # 'red'
print(obj.border) # None
```

###### Methods

| Method Type       | Description |
|-------------------| ----------- |
| Instance methods  | Common type. They always take self as the first positional argument |
| Static methods    | Do not implicitly pass the positional self argument. Static methods are defined by using the `@staticmethod` decorator. Decorators allow us to alter the behavior of functions and classes. |
| Class methods     | Class methods are like instance methods, except that instead of the instance of an object being passed as the first positional self argument, the class itself is passed as the first argument. |

###### Instance Methods

```python
import math
class Circle():
    is_shape = True

    def __init__(self, radius, color='red'):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

# uses
circle = Circle(2)
circle.area() # 12.566370614359172
```

```python
# Like __init__, the __str__ method is another special instance method.
# It is what is displayed when you print the object to the console.
class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq
    
    def __str__(self):
        label = self.name
        if self.population:
            label = '%s, population: %s' % (label, self.population)
        if self.size_kmsq:
            label = '%s, size_kmsq: %s' % (label, self.size_kmsq)
            
        return label
    
obj = Country(name='Japan', population=100)
print(obj) # Japan, population: 100
```


###### Static Methods
```python
import datetime
class Diary():
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas    

    @staticmethod
    def format_date(date):
        return date.strftime('%d-%b-%y')   

    def show_birthday(self):
        return self.format_date(self.birthday)

    def show_christmas(self):
        return self.format_date(self.christmas)

# uses
my_diary = Diary(datetime.date(2020, 5, 14), datetime.date(2020, 12, 25))
my_diary.show_birthday() # '14-May-20'
my_diary.show_christmas() # '25-Dec-20'
```

###### Class Methods
```python
import random
class Pet():
    def __init__(self, height):
        self.height = height        
    is_human = False
    owner = 'John Snow'
    
    @classmethod
    def owned_by_snow_family(cls):
        print(cls.__name__) # Pet
        return 'Snow' in cls.owner
    
    @classmethod
    def create_random_height_pet(cls):
        height = random.randrange(0, 100)
        return cls(height)

print(Pet.owned_by_snow_family()) # Pet (from inside print method), True
for i in range(5):
    pet = Pet.create_random_height_pet()
    print(pet.height) # print random numbers
```

###### Property Decorator
```python
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

# uses
user = Person('John', 'Snow')
# we can use as property, instead of using like a method `user.full_name()` 
user.full_name # 'John Snow'

# Setter
"""
The decorator should be the method name, followed by `.setter`. The name of the setter method should be the same as the name of the property.
"""
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

customer = Person('John', 'Snow')
customer.full_name = 'John Smith'
customer.last_name # Smith
```

###### Inheritance
```python
# Parent Class
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# Child - Baby class is inheriting Person classs
class Baby(Person):
    def speak(self):
        print('Blah blah blah')

# Child - Adult Class
class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)

# uses
priyom = Baby('Priyom', 'Smith')
john = Adult('Jhon', 'Snow')
priyom.speak() # Blah blah blah
john.speak() # Hello, my name is Jhon
```
Multiple inheritance also possible in Python. 
```python
# If we don't need any customization for methods and properties, we can use simply `pass`
class ChildClass(ParentClass1, ParentClass2):
    pass

# If we have the same method in the both `Parent` classes, python reads from left to right in the list of classes.
class Dog():
    def make_sound(self):
        print('Woof!')

class Cat():
    def make_sound(self):
        print('Miaw!')
   
class DogCat(Dog, Cat):
    pass

# uses
my_pet = DogCat()
my_pet.make_sound() # Woof!
```

###### Overriding Methods
```python
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def speak(self):
        print('Hello, my name is %s' % self.first_name)

# Child class
class Guest(Person):
    def speak(self):
        # calling parent class's `speak` method
        super().speak()
        print('It is a pleasure to meet you!')

# uses
john = Guest('John', 'Snow')
john.speak()
```