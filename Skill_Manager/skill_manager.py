print("******** SKILL MANAGER ********")

skills = set()
skills_added = False

menu = 0

while menu != 6:

    print("\n1 → Add Skill")
    print("2 → Display Skills")
    print("3 → Remove Skill")
    print("4 → Check Skill")
    print("5 → Show Number of Skills")
    print("6 → Exit")

    menu = int(input("Enter your option: "))

    # Add Skill
    if menu == 1:

        skills_input = input("Enter skill(s) separated by commas: ")

        new_skills = skills_input.split(",")

        for skill in new_skills:
            skills.add(skill.strip())

        skills_added = True

        print("Skills added successfully!")

    # Display Skills
    elif menu == 2:

        if skills_added:

            print("\n******** SKILLS ********")

            for skill in skills:
                print(skill)

        else:
            print("\nNo skills available. Please add a skill first.")

    # Remove Skill
    elif menu == 3:

        removes = input("Enter the skill to be removed: ")

        if removes in skills:
            skills.remove(removes)
            print("Skill removed successfully!")

        else:
            print("Skill not found.")

    # Check Skill
    elif menu == 4:

        check = input("Enter skill to check: ")

        if check in skills:
            print("The skill is available.")

        else:
            print("Skill not found.")

    # Number of Skills
    elif menu == 5:

        print("Number of Skills:", len(skills))

    # Exit
    elif menu == 6:

        print("\nThank you for using Skill Management System!")

    # Invalid Option
    else:

        print("\nPlease enter a correct option.")