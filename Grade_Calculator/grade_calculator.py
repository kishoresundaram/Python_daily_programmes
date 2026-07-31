print("********GRADE CALCULATOR*************")
m1 = int (input("Enter your  Tamil mark   :"))
m2 = int (input("Enter your  English mark :"))
m3 = int (input("Enter your  Maths mark   :"))
m4 = int (input("Enter your  Science mark :"))
m5 = int (input("Enter your  Social mark  :"))
print("*************************************")

total = m1 + m2 + m3 + m4 + m5
avg = total/5
if avg >= 90:
    print("Congratulations Your grade is A ")
elif 89>= avg >=75:
    print("Keep it up!  Your grade is B ")
elif 74>= avg >=50:
    print("Work hard  Your grade is C ")
else:
      print("Sorry! You have failed.")

  
