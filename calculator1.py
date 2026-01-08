#simple basic calculator

print("my mini project")

num1 = float(input("Enter first number: ")) #2.5
num2 = float(input("Enter second number: ")) #3.7

operation = input("choose operation (+ , - , * , / )")  #+

if operation == '+':
    result = num1 + num2 #6.2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "invalid operation"

print("result:", result) #6.2
print("thankyou so much for looking at it. I hope you will like it")