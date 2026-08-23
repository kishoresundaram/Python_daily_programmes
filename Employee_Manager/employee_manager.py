print("******** EMPLOYEE INFORMATION MANAGER ********")

employee = {
    "name": "Kishore",
    "role": "Python Developer",
    "salary": 25000,
    "experience": 1
}
skills = set()

menu = 0

while menu != 5:

    print("\n1 → Display Employee")
    print("2 → Update Salary")
    print("3 → Add Skill")
    print("4 → Display Skills")
    print("5 → Exit")

    menu = int(input("Enter your option: "))

    if menu == 1:

        print("\n******** EMPLOYEE INFORMATION ********")

        for key, value in employee.items():
            print(key.capitalize(), ":", value)

    elif menu == 2:

        salary = int(input("Enter new salary: "))

        employee["salary"] = salary

        print("Salary updated successfully!")

    elif menu == 3:

        skill_input = input("Enter skill(s) separated by commas: ")

        new_skills = skill_input.split(",")

        for skill in new_skills:
            skills.add(skill.strip())

        print("Skills added successfully!")

    elif menu == 4:

        if len(skills) == 0:
            print("No skills available.")

        else:
            print("\n******** EMPLOYEE SKILLS ********")

            for skill in skills:
                print(skill)

    elif menu == 5:

        print("\nThank you for using Employee Information Manager!")

    else:

        print("\nPlease enter a correct option.")