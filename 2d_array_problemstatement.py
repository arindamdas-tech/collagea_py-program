import numpy as np
marks=np.array([
    [85,96,74],
    [84,54,52],
    [63,45,63],
    [99,66,88],
    [87,69,98],
])
print("Msrks:")
print(marks)

max_marks=np.max(marks)
min_marks=np.min(marks)
Avg_marks=np.mean(marks)

print("maimum Marks:",max_marks)
print("Minimum Msrks:",min_marks)
print("Average Marks:",Avg_marks)

total_marks=np.sum(marks,axis=1)
max_student=np.argmax(total_marks)
min_student=np.argmin(total_marks)

print("Student Id with Maximum total number",max_student)
print("student Id with minimum total number",min_student)