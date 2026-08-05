print("********BMI Calculator*************")
def calculate_bmi(name, weight, height):
    print("****************************")
    bmi = weight / (height * height)
    print("Hello", name)
    print("Your BMI is:", round(bmi, 2))

name = input("Enter Your Name: ")
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

calculate_bmi(name, weight, height)