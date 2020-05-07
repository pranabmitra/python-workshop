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
```