# 🚀 Day 14 – Contact Book Using Python

## 📌 Overview

This is my Day 14 mini project as part of my **#100DaysOfAI learning journey**.

I built a simple Contact Book using Python that allows users to add, view, search, and delete contacts.

The application also uses File Handling to permanently store contact information so that the data is available even after restarting the program.

## 💻 Project Features

The program provides five options:

1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit

### Add Contact

Allows users to enter:

* Name
* Phone Number
* Email

The contact is stored as a Dictionary and saved to a text file.

### View Contacts

Displays all saved contacts.

### Search Contact

Allows users to search for a contact by name.

### Delete Contact

Removes a contact and updates the saved file.

### Persistent Storage

Contacts are stored in `contacts.txt`, allowing data to remain available between program executions.

## 📚 Concepts Used

* Python Lists
* Python Dictionaries
* List of Dictionaries
* File Handling
* `open()`
* Read Mode (`"r"`)
* Write Mode (`"w"`)
* Append Mode (`"a"`)
* `read()`
* `write()`
* `split()`
* `strip()`
* `append()`
* `remove()`
* `len()`
* `for` Loop
* `while` Loop
* `try / except`
* Searching
* Data Persistence

## 🛠️ Technologies & Tools

* Python 3
* Visual Studio Code
* Git & GitHub

## 🖥️ Sample Output

```text
******** CONTACT BOOK ********

1 → Add Contact
2 → View Contacts
3 → Search Contact
4 → Delete Contact
5 → Exit

Enter your option: 1
Enter name: Kishore
Enter phone number: 9876543210
Enter email: kishore@gmail.com

Contact added successfully!

Enter your option: 2

******** CONTACTS ********

Name  : Kishore
Phone : 9876543210
Email : kishore@gmail.com
-------------------------
```

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Store structured information using Dictionaries
* Manage multiple records using Lists
* Save data permanently using text files
* Read previously saved data when the program starts
* Search records using loops
* Delete records and update the stored file
* Handle missing files using exception handling
* Combine multiple Python concepts into one practical application

## 📈 Learning Progress

* ✅ Day 8 – Python Lists – Student List Manager
* ✅ Day 9 – Python Tuples – Employee Records
* ✅ Day 10 – Python Sets – Skill Manager
* ✅ Day 11 – Python Dictionaries – Employee Information Manager
* ✅ Day 12 – Python Collections – Expense Tracker
* ✅ Day 13 – Python File Handling – Notes Manager
* ✅ Day 14 – Lists + Dictionaries + File Handling – Contact Book

## 🚀 Next Step

Next, I will continue building practical Python projects and strengthen my understanding of data handling and programming fundamentals.

## 📖 My #100DaysOfAI Journey

This project is part of my **100 Days of AI learning journey**, where I am building strong programming fundamentals through consistent hands-on practice in Python, Machine Learning, and Generative AI.
