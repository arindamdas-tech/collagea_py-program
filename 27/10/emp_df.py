import pandas as pd

data = {
    'Emp_ID': [101, 102, 103, 104, 105],
    'Emp_Name': ['Rahul', 'Amit', 'Raju', 'Sima', 'Rohan'],
    'Salary': [25000, 30000, 45000, 35000, 50000]
}

df = pd.DataFrame(data)

# First two records
print("First two records:")
print(df.head(2))

# Last two records
print("\nLast two records:")
print(df.tail(2))

# Employee having maximum salary
print("\nEmployee with maximum salary:")
print(df[df['Salary'] == df['Salary'].max()])