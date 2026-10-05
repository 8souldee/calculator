print("Blast Calculator")

a=float(input("Enter the first number: "))
operator=input("Enter the operation (+, -, *, /): ")
b=float(input("Enter the second number: "))

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print("The result is:", result) 