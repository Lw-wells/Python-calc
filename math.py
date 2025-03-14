number = int(input("Enter first number:"))

number2 = int(input("Enter second number:"))

operator = input("Input operator, (+/-/*or /):")

if operator == "+":
    result = number + number2

elif operator == "-":
    result = number - number2

elif operator == "*":
    result = number * number2

elif operator == "/":
    result = number / number2 

else :
    print("Invalid opertaor")



print(f"{number} {operator} {number2} = {result}")