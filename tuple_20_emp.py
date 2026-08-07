# Create a tuple of 20 employee names
employees = (
    "Amit", "Rahul", "Priya", "Sneha", "Amit",
    "Riya", "Rahul", "Karan", "Neha", "Rohan",
    "Priya", "Amit", "Suman", "Riya", "Ankit",
    "Rohan", "Rahul", "Pooja", "Karan", "Amit"
)

print("Employee Tuple:")
print(employees)
print("\nFrequency of each employee:")
unique_names = set(employees)
for name in unique_names:
    print(name, ":", employees.count(name))

# ii) Remove duplicate items and find number of distinct* names
distinct_names = tuple(set(employees))
print("\nTuple after removing duplicates:")
print(distinct_names)

print("Number of distinct names:", len(distinct_names))

# iii) Print the employee having maximum frequency
max_name = employees[0]
max_count = employees.count(max_name)

for name in unique_names:
    if employees.count(name) > max_count:
        max_name = name
        max_count = employees.count(name)

print("\nEmployee with maximum frequency:")
print(max_name, "-", max_count, "times")

# iv) Sort the tuple alphabetically
sorted_tuple = tuple(sorted(employees))
print("\nTuple in alphabetical order:")
print(sorted_tuple)

# v) Search for an employee name
search = input("\nEnter employee name to search: ")

if search in employees:
    print(search, "exists in the tuple.")
else:
    print(search, "does not exist in the tuple.")