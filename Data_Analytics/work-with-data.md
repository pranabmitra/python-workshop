##### Dataset

A dataset is a collection of data.

Here we'll work on Boston Housing dataset.

```python
import pandas as pd

# Pandas converts the data into a DataFrame upon reading it
housing_df = pd.read_csv('data/HousingData.csv')
housing_df.head() # select first five rows by default
housing_df.head(10) # to modify the selection (select 10 rows)

# to display key statistical measures of each column, including the mean, median, and quartiles...
housing_df.describe()

# deliver a full list of columns.info(). It reveals the non-null values of each column
housing_df.info()

# get the number of rows and columns
housing_df.shape

# find values and columns in the dataset with null values
"""
The .isnull() method will display an entire DataFrame of True/False values depending on the Null value. Give it a try. The .any() method returns the individual columns.
"""
housing_df.isnull().any()
```

###### Replacing Null Values
Pandas has `fillna` method, which can be used to replace null values. It works for individual columns and entire DataFrames. 
There are 3 approaches:
* replacing the null values of a column with the mean
* replacing the null values of a column with another value
* replacing all the null values in the entire dataset with the median

```python
# replace null column values with mean:
housing_df['AGE'] = housing_df['AGE'].fillna(housing_df.mean())

# replace null column values with a value (0 in this case)
housing_df['CHAS'] = housing_df['CHAS'].fillna(0)

# replace null DataFrame values with median
housing_df = housing_df.fillna(housing_df.median())

housing_df.isnull().any() # will return false for every column
```

###### Data Visualization

```python
import matplotlib.pyplot as plt
# `%matplotlib` inline ensures that your graphs appear in the Jupyter Notebook instead of external files.
%matplotlib inline

# `seaborn` - will make the graph more visually appealing
import seaborn as sns
# set up seaborn dark grid
sns.set()

# plot the histogram fo
plt.hist(housing_df['MEDV'])
plt.show()
```

###### Create a `show_hist` method to use with different column
```python
def show_hist(column, title, xlab, ylab):
    plt.figure(figsize=(10,6))
    plt.hist(column)
    plt.title(title, fontsize=15)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.savefig(title, dpi=300)
    plt.show()

# call our function
show_hist(housing_df['RM'], 'Average Number of Rooms in Boston Households', 'Average Number of Rooms', 'Count')
```

###### Correlation
Correlation is a statistical measure between -1 and +1 that indicates how closely two variables are related.

```python
# find the correlation value of the dataset
housing_df.corr()
```

> Seaborn provides a nice way to view correlations, called a *heatmap*
```python
corr = housing_df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, xticklabels=corr.columns.values, 
yticklabels=corr.columns.values, cmap="Blues", linewidths=1, alpha=0.8)
plt.show()
```

###### Regression
```python
x = housing_df['RM']
y = housing_df['MEDV']
plt.figure(figsize=(10, 7))
sns.regplot(x,y)
plt.show()
```

###### Box plot and Violin plot
```python
# box plot
x = housing_df['RM']
y = housing_df['MEDV']
plt.boxplot(x)
plt.show()


# violin plot
plt.violinplot(x)
plt.show()
```