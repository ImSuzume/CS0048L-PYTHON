#Problem 1
print ((14*12)/(33*144-187))

#Problem 2
dist_KM = eval(input("Enter distance in KM: "))
print(f"The distance in miles is {(dist_KM*0.621371):0.5f}.")

#Problem 3
name = input("Enter your name")
print(name,name,name)

#Problem 4
Num1 = eval(input("Enter 1st Number: "))
Num2 = eval(input("Enter 2nd Number: "))
print(f"The sum of {Num1} and {Num2} is {Num1+Num2}.")

#Problem 5
Height = eval(input("Enter your height in inches: "))
Weight = eval(input("Enter your weight in lb: "))
BMI = (703*Weight)/(pow(Height,2))
print(f"Your BMI is {BMI:.2f}.")

#Problem 6
Num1 = eval(input("Enter 1st Number: "))
Num2 = eval(input("Enter 2nd Number: "))
Num3 = eval(input("Enter 3rd Number: "))
Num4 = eval(input("Enter 4th Number: "))
Num5 = eval(input("Enter 5th Number: "))
print(Num1,Num2,Num3,Num4,Num5, sep="   ")

#Problem 7
VarNum = eval(input("Enter any number: "))
VarNum += 2
print(f"{VarNum}")
