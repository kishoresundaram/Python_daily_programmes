print("******** NOTES MANAGER ********")

menu = 0

while menu != 4:

    print("\n1 → Add Note")
    print("2 → View Notes")
    print("3 → Clear Notes")
    print("4 → Exit")

    menu = int(input("Enter your option: "))

    if menu == 1:

        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note added successfully!")

    elif menu == 2:

        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

                if notes:
                    print("\n******** YOUR NOTES ********")
                    print(notes)
                else:
                    print("\nNo notes available.")

        except FileNotFoundError:
            print("\nNo notes available.")

    elif menu == 3:

        with open("notes.txt", "w") as file:
            file.write("")

        print("All notes cleared successfully!")

    elif menu == 4:

        print("\nThank you for using Notes Manager!")

    else:

        print("\nPlease enter a correct option.")