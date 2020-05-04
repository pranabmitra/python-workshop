#### Plotting techniques

###### Defensive code
```python
"""
Defensive programming is a form of debugging approach that ensures the continuing function of a piece of a program
"""
x = 2
assert x < 1, "Invalid value"
```
### Plot
*Import the lib:*
```python
import matplotlib.pyplot as plt
```

###### _Scatter plot:_
```python
# Dataset
temperature = [14.2, 16.4, 11.9, 12.5, 18.9, 22.1, 19.4, 23.1, 25.4, 18.1, 22.6, 17.2]
sales = [215.20, 325.00, 185.20, 330.20, 418.60, 520.25, 412.20, 614.60, 544.80, 421.40, 445.50, 408.10]

plt.title('Ice-cream sales versus Temperature')
plt.xlabel('Temperature')
plt.ylabel('Sales')
plt.scatter(temperature, sales, color='red')
plt.show()
```

###### _Line Chart:_
```python
data = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85]

plt.plot(data)
plt.title('Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')
plt.show()

# Due to zero based index, we can see the graph started from 0. 
# If we want to show it from 1, we can do the following:

data = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85]

t = list(range(1, len(data) + 1)) 

plt.title('Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')

plt.plot(t, data, marker='.')
plt.xticks([1, 3, 5, 8, 10]) 

plt.show()
```

###### _Bar Chart:_
```python
grades = ['A', 'B', 'C', 'D', 'E', 'F']
students_count = [20, 30, 10, 5, 8, 2]

plt.title('Grades Bar Plot for Biology Class')
plt.xlabel('Grade')
plt.ylabel('Num Students')

plt.bar(grades, students_count)
plt.show()

# Horizontal Bars with different bar colors
plt.barh(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])
```

Although, histograms and bar plots look the same, he main difference between a histogram and a bar plot is that there is no space between the adjacent columns in a histogram.

###### _Pie Chart:_
```python
labels = ['Monica', 'Adrian', 'Jared']
num = [230, 100, 98] # Note that this does not need to be percentages
plt.title('Voting Results: Club President', fontdict={'fontsize': 20})

plt.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
plt.show()
```

###### _Heatmap:_
```python
import numpy as np
import matplotlib.pyplot as plt

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    # if no ax object exists, get current axis from plot
    if not ax:
        ax = plt.gca()
    im = ax.imshow(data, **kwargs)
    
    # define the color bars
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    
    # show all ticks and labels
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    
    # configure horizontal axes labelling appear on top
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")
    
    # turn off spine and create a white grid
    for edge, spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    
    # return image and colorbar
    return im, cbar

# Dataset
data = np.array([
    [30, 20, 10,],
    [10, 40, 15],
    [12, 10, 20]
])
im, cbar = heatmap(data, ['Class-1', 'Class-2', 'Class-3'], ['A', 'B', 'C'], cmap='YlGn', cbarlabel='Number of Students')
```

###### _Density plot:_
```python
import seaborn as sns
import matplotlib.pyplot as plt

data = [90, 80, 50, 42, 89, 78, 34, 70, 67, 73, 74, 80, 60, 90, 90]

plt.title('Density Plot')
plt.xlabel('Score')
plt.ylabel('Density')

sns.distplot(data)
plt.show()
```

###### _Contour plot:_
```python
import seaborn as sns
import matplotlib.pyplot as plt

weight=[85.08,79.25,85.38,82.64,80.51,77.48,79.25,78.75,77.21,73.11,82.03,82.54,74.62,79.82,79.78,77.94,83.43,73.71,80.23,78.27,78.25,80.00,76.21,86.65,78.22,78.51,79.60,83.88,77.68,78.92,79.06,85.30,82.41,79.70,80.16,81.11,79.58,77.42,75.82,74.09,78.31,83.17,75.20,76.14]

plt.legend(labels=['a', 'b'])
plt.title('Weight Dataset - Contour Plot')
plt.ylabel('height (cm)')
plt.xlabel('width (cm)')

sns.kdeplot(list(range(1,45)),weight, kind='kde', cmap="Reds")
```

###### _Multiple plots:_
```python
import matplotlib.pyplot as plt
# Split the figure into 2 subplots
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121) # 121 means split into 1 row , 2 columns, and put in 1st part.
ax2 = fig.add_subplot(122) # 122 means split into 1 row , 2 columns, and put in 2nd part.
labels = ['Adrian', 'Monica', 'Jared']
num = [230, 100, 98]

ax1.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
ax1.set_title('Pie Chart (Subplot 1)')
# Plot Bar Chart (Subplot 2)
plt.bar(labels, num, color=['lightblue', 'lightgreen', 'yellow'])
ax2.set_title('Bar Chart (Subplot 2)')
ax2.set_xlabel('Candidate')
ax2.set_ylabel('Votes')

fig.suptitle('Voting Results', size=14)
```

###### _3D plot:_
```python
# Plot a Sine Wave
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
# Add title and axes labels
ax.set_title("Demo of 3D Plot", size=13)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
```