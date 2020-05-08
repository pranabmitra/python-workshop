#### Standart Libraries

###### Timezone
```python
import datetime
from dateutil import tz

d1 = datetime.datetime(2019, 4, 24, hour=11, tzinfo=tz.gettz("Europe/Madrid"))

d2 = datetime.datetime(2019, 4, 24, hour=8, tzinfo=tz.gettz("America/Los_Angeles"))

print(d1.hour > d2.hour) # True
print(d1 > d2) # False; Due to timezone

# convert tz
d2_madrid = d2.astimezone(tz.gettz("Europe/Madrid"))
print(d2_madrid.hour) # 17; That's why d1 > d2 = False

# It's better to use UTC to keep datetime in a common format
# Delta (difference between two datetime)
import datetime as dt

d1 = dt.datetime(2019, 2, 25, 10, 50,
                 tzinfo=dt.timezone.utc)
d2 = dt.datetime(2019, 2, 26, 11, 20,
                 tzinfo=dt.timezone.utc)

td = d2 - d1
print(td) # 1 day, 0:30:00
td.total_seconds() # 88200.0

# Current time
d1 = dt.datetime.now() # Current local time
# A common way to serialize datetimes is by encoding them in a string using
d1.isoformat() # '2020-05-07T00:51:39.305404'

d1 = dt.datetime.now(dt.timezone.utc) # Current time in UTC
d1.isoformat() # '2020-05-06T15:51:25.554716+00:00'
```

###### Time
```python
"""
Calculate the elapsed time
"""
import random
import time

start = time.time()
# do whatever you want to check the execution time
l = [random.randint(1, 999) for _ in range(10 * 5)]
end = time.time()
print(end - start)
```


###### OS
```python
# os info
import os

print("Process id:", os.getpid())
print("Parent process id:", os.getppid())
# access environment variable
print(os.environ) # print the dict for all env vars
print(os.environ['HOME'])
print(os.getcwd()) # current working directory 

# platform info
import platform

print("Machine network name:", platform.node())
print("Python version:", platform.python_version())
print("System:", platform.system())

# sys info
import sys

print("Python module lookup path:", sys.path)
print("Command to run Python:", sys.argv)

# pathlib (glob pattern)
import pathlib
p = pathlib.Path("").cwd()
print(p) # current working directory

txt_files = p.glob("*.txt")
print("*.txt:", list(txt_files)) # all *.txt files from the current directory

# To get the all hidden files from the HOME directory
import pathlib
p = pathlib.Path.home()
print(list(p.glob(".*")))
```

###### Logging
```python
import logging

logger = logging.getLogger("logger_name")

logger.debug("Logging at debug")
logger.info("Logging at info")
logger.warning("Logging at warning")
logger.error("Logging at error")
logger.fatal("Logging at fatal")

# example
import logging

try:
    int("nope")
except Exception:
    logging.error("Something bad happened", exc_info=True)
# Because of using `exc_info=True`, it will print the Traceback with details
```


###### Collections
Besides the basic collections (list, dict, tuple, and set), we have some advanced collections (counter, defauldict, and chainmap) in python.

- Counter:
A counter is a class that allows us to count hashable objects. It has keys and values as a dictionary (it actually inherits from dict) to store objects as keys and the number of occurrences in values.

```python
# Counter
import urllib.request

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = urllib.request.urlopen(url)
words = response.read().decode().split()
len(words)  # 858

import collections
word_counter = collections.Counter(words)

for word, count in word_counter.most_common(5):
    print(word, "-", count)

# we can print the word count like below:
print("PYTHON", "-", word_counter["PYTHON"])
```

- defaultdict
This class behaves like a dict but allows us to provide a factory method to be used when a key is missing.
```python
import collections

data = collections.defaultdict(int)
"""
Whether `x` is in `data` or not, we don't need to consider.
"""
def function(x):
    data[x] += 1
```

- ChainMap
ChainMap is a structure that allows us to combine lookups for multiple mapping objects, usually dictionaries. It can be seen as a multi-level object.

```python
import collections

_defaults = {
    "appetizers": "Hummus",
    "main": "Pizza",
    "desert": "Chocolate cake",
    "drink": "Water",
}

def prepare_menu(customizations):
    return collections.ChainMap(customizations, _defaults)

def print_menu(menu):
    for key, value in menu.items():
        print(f"As {key}: {value}.")

# uses
menu1 = prepare_menu({})
print_menu(menu1)

# customized menu
menu2 = prepare_menu({"drink": "Red Wine", "side": "French fries"})
print_menu(menu2)
```