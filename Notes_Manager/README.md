# 🚀 Day 13 – Notes Manager Using Python File Handling

## 📌 Overview

This is my Day 13 mini project as part of my **#100DaysOfAI learning journey**.

I built a simple menu-driven Notes Manager using Python File Handling. The application allows users to add notes, view saved notes, and clear notes stored in a text file.

Unlike previous projects where data was lost after the program stopped, this project stores notes permanently in a file.

## 💻 Project Features

The program provides four options:

1. Add Note
2. View Notes
3. Clear Notes
4. Exit

### Add Note

Allows users to enter a note and saves it to `notes.txt`.

### View Notes

Reads and displays all saved notes.

### Clear Notes

Removes all notes from the file.

### Exit

Safely exits the application.

## 📚 Concepts Used

- Python File Handling
- `open()`
- `with open()`
- Read Mode (`"r"`)
- Write Mode (`"w"`)
- Append Mode (`"a"`)
- `read()`
- `write()`
- Exception Handling
- `try / except`
- `while` Loop
- Conditional Statements

## 🛠️ Technologies & Tools

- Python 3
- Visual Studio Code
- Git & GitHub

## 🖥️ Sample Output

```text
******** NOTES MANAGER ********

1 → Add Note
2 → View Notes
3 → Clear Notes
4 → Exit

Enter your option: 1
Enter your note: Learn Python File Handling

Note added successfully!

Enter your option: 2

******** YOUR NOTES ********
Learn Python File Handling
