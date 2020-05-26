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
```