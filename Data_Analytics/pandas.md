##### Pandas

_
Pandas can import data, read data, and display data in an object called a DataFrame. A DataFrame consists of rows and columns.
_

```python
import pandas as pd
```

```python
# create a dictionary
dict = {'A':[63, 75, 88], 'B':[48, 98, 92], 'C': [87, 86, 85]}
# create DataFrame
df = pd.DataFrame(dict)
print(df)
#  Output:
#     A   B   C
# 0  63  48  87
# 1  75  98  86
# 2  88  92  85

df = df.T # transpose: turns rows into columns and columns into rows.
print(df) 
#     0   1   2
# A  63  75  88
# B  48  98  92
# C  87  86  85

# rename columns
df.columns = ['Quiz_1', 'Quiz_2', 'Quiz_3']
print(df)
#    Quiz_1  Quiz_2  Quiz_3
# A      63      75      88
# B      48      98      92
# C      87      86      85

print(df.iloc[0]) # first row
# Quiz_1    63
# Quiz_2    75
# Quiz_3    88

print(df.iloc[0, 1]) # first row, second column
# 75

# access first column by following ways:
df.Quiz_1
df['Quiz_1']
df.iloc[:, 0]
# output
# A    63
# B    48
# C    87

df.iloc[1:, 0]
# B    48
# C    87

# add new column: axis: 0 = index; 1 = rows
df['Quiz_Avg'] = df.mean(axis=1)
# delete column
del df['Quiz_Avg']

"""
To add new rows to a pandas DataFrame, a common strategy is to generate a new DataFrame and then to concatenate the values.
"""
# create new DataFrame of one row
df_new = pd.DataFrame({'Quiz_1':[np.NaN], 'Quiz_2':[np.NaN], 'Quiz_3': [72]}, index=['D'])
# concatenate DataFrames
df = pd.concat([df, df_new])
print(df)
#    Quiz_1  Quiz_2  Quiz_3
# A    63.0    75.0      88
# B    48.0    98.0      92
# C    87.0    86.0      85
# D     NaN     NaN      72

# `skipna` - to ignore the NaN value
df['Quiz_Avg'] = df.mean(axis=1, skipna=True)
df
"""
	Quiz_1	Quiz_2	Quiz_3	Quiz_Avg
A	63.0	75.0	88	75.333333
B	48.0	98.0	92	79.333333
C	87.0	86.0	85	86.000000
D	NaN	NaN	72	72.000000
"""
```

