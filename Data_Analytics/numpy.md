##### NumPy

###### Convert list to Numpy array

```python
list = [70,65,95,88]
type(list) # list

import numpy as np

scores = np.array(list)
type(scores) # numpy.ndarray

# mean value 
scores.mean() # 79.5
# or, 
np.mean(scores) # 79.5

# median value
np.median(scores) # 79
# standard deviation
scores.std() # 12.379418403139947

scores.max() # 95
scores.min() # 65
scores.sum() # 318
```

###### Dataframes
```python
import numpy as np 
np.random.seed(seed=60)
matrix = np.random.rand(3,3)
print(matrix)
# output
[[0.30087333 0.18694582 0.32318268]
 [0.66574957 0.5669708  0.39825396]
 [0.37941492 0.01058154 0.1703656 ]]

# first row
matrix[0] # [0.77132064 0.02075195 0.63364823]
matrix[0, :]
# first column
matrix[:, 0] # [0.77132064, 0.74880388, 0.19806286]

# 1st row, 1st column
martix[0, 0] # 0.771320643266746
matrix[0][0] # 0.771320643266746

# 1st row, 3rd column
matrix[0][2] # 0.6336482349262754 
matrix[0, 2] # 0.6336482349262754

# mean
matrix.mean() # 0.4472814201606212
# last column
matrix[:, -1] # [0.63364823, 0.22479665, 0.16911084]
matrix[:, -1].mean() # 0.3425185723398862
```

###### Time coputation for a large matrix
```python
# computation time for the mean of the matrix
%%time
big_matrix = np.random.rand(100000, 100)
big_matrix.mean()
```

###### Creating Array using NumPy
```python
import numpy as np
# generate 100 (1, 100) length array
np.arange(1, 101)
# [1,2,3,....100]

np.arange(1, 101, 5) # length: 20
# [ 1,  6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]

# generate 10*10 array
np.arange(1, 101).reshape(10,10)
np.arange(1, 101, 5).reshape(4, 5)
# array([[ 1,  6, 11, 16, 21],
#       [26, 31, 36, 41, 46],
#       [51, 56, 61, 66, 71],
#       [76, 81, 86, 91, 96]])

mat = np.arange(1, 101, 5).reshape(4,5)
# we can do the following operations to add, square the matrix
mat + mat
mat * 2
mat * mat
mat.T # transpose: turns rows into columns and columns into rows
# array([[ 1, 26, 51, 76],
#       [ 6, 31, 56, 81],
#       [11, 36, 61, 86],
#       [16, 41, 66, 91],
#       [21, 46, 71, 96]])

```