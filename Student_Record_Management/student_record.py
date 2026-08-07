print("******** STUDENT MANAGEMENT SYSTEM ********")

name = ""
age = 0
department = ""
student_added = False


def add_student(name, age, department):
    print("\nStudent added successfully!")
    print("Name       :", name)
    print("Age        :", age)
    print("Department :", department)


def display_student(name, age, department):
    print("\n******** Student Details ********")
    print("Name       :", name)
    print("Age        :", age)
    print("Department :", department)


menu = 0

while menu != 3:

    print("\n1 → Add Student")
    print("2 → Display Student")
    print("3 → Exit")

    menu = int(input("Enter your option: "))

    if menu == 1:
        name = input("Enter Your Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")

        add_student(name, age, department)
        student_added = True

    elif menu == 2:

        if student_added:
            display_student(name, age, department)
        else:
            print("\nNo student details available. Please add a student first.")

    elif menu == 3:
        print("\nThank you for using Student Management System!")

    else:
        print("\nPlease enter a correct option.")