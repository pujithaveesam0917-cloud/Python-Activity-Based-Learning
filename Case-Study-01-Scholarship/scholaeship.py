print("UNIVERSITY SCHOLARSHIP ALLOCATION")

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    m1 = int(input("Enter marks in subject 1: "))
    m2 = int(input("Enter marks in subject 2: "))
    m3 = int(input("Enter marks in subject 3: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total = m1 + m2 + m3
    aggregate = total / 3

    if (m1 >= 40 and m2 >= 40 and m3 >= 40
            and aggregate >= 75
            and attendance >= 75
            and income <= 250000):
        print(name, "is eligible for scholarship")
        print("Aggregate:", aggregate)
    else:
        print(name, "is not eligible for scholarship")
