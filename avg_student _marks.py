marks = [78, 85, 92, 67, 88, 95, 73, 81, 90, 76]
average = sum(marks) / len(marks)
print("Average Marks =", average)
count = 0
for mark in marks:
    if mark > average:
        count += 1

print("Number of students scoring more than average =", count)
maximum = max(marks)
print("Maximum Marks =", maximum)