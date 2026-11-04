import pandas as pd

# Import the dataset
df = pd.read_csv(r"C:\Users\darin\Downloads\titanic\test_data.csv")

# 1. Clean the dataset and print the result
df = df.dropna()
print("Cleaned Dataset:")
print(df)

# 2. Find passengers whose age is more than 40 and are female
result = df[(df["Age"] > 40) & (df["Sex"] == "female")]
print("\nFemale passengers older than 40:")
print(result)

# 3. Describe passengers belonging to Passenger Class 1
result = df[df["Pclass_1"] == 1]
print("\nPassenger Class 1 Details:")
print(result.describe())

# 4. Remove duplicate Passenger IDs
df = df.drop_duplicates(subset=["PassengerId"])
print("\nDataset after removing duplicates:")
print(df)

# 5. Insert a new column into the dataset
df.insert(1, "Status", "Passenger")
print("\nDataset after inserting a new column:")
print(df)

# Save the final dataset
df.to_csv(r"C:\Users\darin\Downloads\titanic.csv", index=False)