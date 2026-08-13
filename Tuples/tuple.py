employee1 = ("Kishore", "Python Developer", 25000)
employee2 = ("Rahul", "Data Analyst", 28000)
employee3 = ("Arun", "AI Engineer", 35000)

employees = (employee1, employee2, employee3)


print("Total employees:",len(employees))

for name, role, salary in employees:
    print("Name       :", name)
    print("Role       :", role)
    print("Salary     :", salary)
    print()