# 🚀 Day 10 – Skill Manager Using Python Sets

## 📌 Overview

This is my Day 10 mini project as part of my **#100DaysOfAI learning journey**.

I built a simple menu-driven **Skill Manager using Python Sets** that allows users to add, display, remove, search, and count technical skills.

The program also allows users to enter multiple skills at once using commas, while the Set automatically removes duplicate skills.

## 💻 Project Features

The program provides six options:

1. Add Skill
2. Display Skills
3. Remove Skill
4. Check Skill
5. Show Number of Skills
6. Exit

### Add Skills

Allows users to enter one or multiple skills separated by commas.

Example:

```text
Python, SQL, Java, Git, Python
```

The duplicate `Python` is automatically removed because Sets store only unique values.

### Display Skills

Displays all skills currently stored in the Set.

### Remove Skill

Allows the user to remove a specific skill.

### Check Skill

Checks whether a particular skill exists in the Set.

### Show Number of Skills

Displays the total number of unique skills using `len()`.

## 📚 Concepts Used

* Python Sets
* `set()`
* `add()`
* `remove()`
* `in` operator
* `len()`
* `split()`
* `strip()`
* `for` loop
* `while` loop
* Conditional Statements
* User Input
* Duplicate Removal

## 🛠️ Technologies & Tools

* Python 3
* Visual Studio Code
* Git & GitHub

## 🖥️ Sample Output

```text
******** SKILL MANAGER ********

1 → Add Skill
2 → Display Skills
3 → Remove Skill
4 → Check Skill
5 → Show Number of Skills
6 → Exit

Enter your option: 1
Enter skill(s) separated by commas: Python, SQL, Java, Python, Git

Skills added successfully!

Enter your option: 5
Number of Skills: 4
```

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Create and use Python Sets
* Store unique values
* Automatically handle duplicate data
* Add and remove elements from a Set
* Search for values using the `in` operator
* Count elements using `len()`
* Process multiple user inputs using `split()`
* Remove unwanted spaces using `strip()`
* Build a practical menu-driven application

## 📈 Week 2 Progress

* ✅ Day 8 – Python Lists – Student List Manager
* ✅ Day 9 – Python Tuples – Employee Records
* ✅ Day 10 – Python Sets – Skill Manager

## 🚀 Next Step

Next, I will continue learning Python Collections with **Dictionaries** and explore how key-value pairs can be used to organize structured data.

## 📖 My #100DaysOfAI Journey

This project is part of my **100 Days of AI learning journey**, where I am building strong programming fundamentals through consistent hands-on practice in Python, Machine Learning, and Generative AI.
