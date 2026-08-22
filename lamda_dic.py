student={
    "arindam":89,
    "Asif":86,
    "Mominul":55,
    "wasif":80,
    "avik":88,
    
}
sorted_element=dict(sorted(student.items(),key=lambda x:x[1],reverse=True))
print("Sorted according mask :")
print(sorted_element)

maximum_marks=max(student.items(), key=lambda x:x[1])
print("maximum of the student marks")
print(maximum_marks)

average=sum(student.values())/len(student)
print("\nAverage marks",average)

print("\nStudent having marks more than average")
for name,marks in student.items():
    if marks>average:
        print(name,":",marks)