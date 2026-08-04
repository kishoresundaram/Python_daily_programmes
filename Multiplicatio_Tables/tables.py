# Program: Multiplication Table
# Day 5 - Python Loops

num = int(input("Enter the number: "))

print("\n***** Multiplication Table *****")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)