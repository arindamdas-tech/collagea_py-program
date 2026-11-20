import pandas as pd
import numpy as np

data = {
    'Roll': [1, 2, 3, 4, 5],
    'Name': ['Sima', 'Binita', 'Raju', 'Rahul', 'Amit'],
    'Dept': [None, 'CSE', 'ECE', None, 'IT'],
    'Marks': [85, 90, 75, 80, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.isnull().any())
df.loc[df['Name'] == 'Sima', 'Dept'] = 'CSE'

print(df)
df = df.dropna()

print(df)
df = df.dropna()

print(df)