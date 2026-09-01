print("******** CONTACT BOOK ********")

contacts = []

# Load existing contacts from file
try:
    with open("contacts.txt", "r") as file:

        for line in file:
            data = line.strip().split(",")

            if len(data) == 3:
                contact = {
                    "name": data[0],
                    "phone": data[1],
                    "email": data[2]
                }

                contacts.append(contact)

except FileNotFoundError:
    pass


menu = 0

while menu != 5:

    print("\n1 → Add Contact")
    print("2 → View Contacts")
    print("3 → Search Contact")
    print("4 → Delete Contact")
    print("5 → Exit")

    menu = int(input("Enter your option: "))

    # Add Contact
    if menu == 1:

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        with open("contacts.txt", "a") as file:
            file.write(name + "," + phone + "," + email + "\n")

        print("Contact added successfully!")

    # View Contacts
    elif menu == 2:

        if len(contacts) == 0:
            print("\nNo contacts available.")

        else:
            print("\n******** CONTACTS ********")

            for contact in contacts:

                print("Name  :", contact["name"])
                print("Phone :", contact["phone"])
                print("Email :", contact["email"])
                print("-------------------------")

    # Search Contact
    elif menu == 3:

        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:

            if contact["name"].lower() == search_name.lower():

                print("\nContact Found!")
                print("Name  :", contact["name"])
                print("Phone :", contact["phone"])
                print("Email :", contact["email"])

                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete Contact
    elif menu == 4:

        delete_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:

            if contact["name"].lower() == delete_name.lower():

                contacts.remove(contact)
                found = True

                # Rewrite file after deletion
                with open("contacts.txt", "w") as file:

                    for item in contacts:
                        file.write(
                            item["name"] + ","
                            + item["phone"] + ","
                            + item["email"] + "\n"
                        )

                print("Contact deleted successfully!")
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif menu == 5:

        print("\nThank you for using Contact Book!")

    else:

        print("\nPlease enter a correct option.")