print("******** STUDENT LIST MANAGER ********")

students = []

menu = 0

while menu != 5:

    print("\n1 → Add Student")
    print("2 → Display Students")
    print("3 → Remove Student")
    print("4 → Show Number of Students")
    print("5 → Exit")

    menu = int(input("Enter your option: "))

    if menu == 1:
        name = input("Enter student name: ")

        students.append(name)

        print("Student added successfully!")

    elif menu == 2:

        if len(students) == 0:
            print("No students available.")

        else:
            print("\n******** STUDENTS ********")

            for student in students:
                print(student)

    elif menu == 3:

        if len(students) == 0:
            print("No students available to remove.")

        else:
            name = input("Enter student name to remove: ")

            if name in students:
                students.remove(name)
                print("Student removed successfully!")
            else:
                print("Student not found.")

    elif menu == 4:

        print("Number of Students:", len(students))

    elif menu == 5:
        print("Thank you for using Student List Manager!")

    else:
        print("Please enter a correct option.")