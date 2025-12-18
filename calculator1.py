#simple basic calculator

print("my mini project")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("choose operation (+ , - , * , / )")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "invalid operation"

print("result:", result)
print("thankyou so much for looking at it. I hope you will like it")