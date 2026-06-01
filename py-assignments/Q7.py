students = {}

n = int(input("Enter Number of Students: "))

for i in range(n):

    name = input("Enter Student Name: ")

    marks = int(input("Enter Marks: "))

    students[name] = marks

print("\nStudent Records")

for name, marks in students.items():
    print(name, ":", marks)