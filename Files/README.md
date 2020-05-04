#### File operations

###### File mode
| Mode | Description |
|------| ------------|
| 'R'  | Default mode. This opens a file for reading.|
| 'W'  | Write mode. This opens a file for writing, creates a new file if the file does not exist, and overwrites the content if the file already exists. |
| 'X'  | Create a new file. The operation fails if the file exists. |
| 'A'  | Open a file in Append mode. It creates a new file if the file doesn't exist. |
| 'B'  | Open the file in Binary mode |

###### Read a file
```python
# Simple file read operation
f = open('filename.txt')
text = f.read()
print(text)

"""
The with statement is a control flow structure of Python. It guarantees that the preceding file object, f, will close automatically after the code block exits, no matter how the nested block exits.

If an exception occurs before the end of the block, it will still close the file before the exception is caught. Of course, it will close the file even if the nested block runs successfully.
"""
# Read the few characters
with open("filename.txt") as f:
    print(f.read(6))

# Read the first line
with open("filename.txt") as f:
    print(f.readline())
```

###### Write a file
```python
f = open('log.txt', 'w')

from datetime import datetime
import time
for i in range(0,10):
    # print the same output in the console
    print(datetime.now().strftime('%Y%m%d_%H:%M:%S - '), i)

    # writing in the file
    f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S - '));
    # to wait for 1 sec
    time.sleep(1)
    f.write(str(i));
    f.write("\n")
f.close()
```
