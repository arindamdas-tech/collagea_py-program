students=["Arindam", "wasif", "mominul", "Asif", "Rajjak", "mojamel", "Rohit", "virat", "kabir", "arijit"]
marks =[]
print("Enter the marks of the student")
for student in students:
    while True:
        mark = int(input(f"Enter the marks of {student}: "))
        if mark in marks :
            print("duplicate marks are not allowed. Please enter a unique mark.")
        else:
            marks.append(mark)
            break
max_num = max(marks)
min_num = min(marks)
max_student = students[marks.index(max_num)]
min_student = students[marks.index(min_num)]
print("\n student marks ")
for i in range(len(students)):
    print(f"{students[i]}: {marks[i]}")
    
    
print(max_student, "=", max_num)
print(min_student, "=", min_num)
