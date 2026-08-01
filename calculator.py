
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation you wanna perform: + , - , * , /")

operator = input("Enter your choice of operation: ")

if operator == '+':
    print("result is", num1 + num2)
elif operator == '-':
    print("result is", num1 - num2)
elif operator == '*':
    print("result is", num1 * num2)
elif operator == '/':
    print("result is", num1 / num2)
   
else:
    print("Invalid choice! Please select a valid operator.")
