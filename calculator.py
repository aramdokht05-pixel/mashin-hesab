print(" ---New calculator--- ")
print(" hello, welcome... ")
print(" type 'exit' to quit\n")

import math

while True:
    num1 = float(input(" first number: "))
    op = input(" ( /, *, -, +, ** ) ")

    if op == "exit":
        print("Goodbye!")
        break

    num2 = float(input(" second number: "))

    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2
    elif op == "/":
        if num2 != 0:
            answer = num1 / num2
        else:
            answer = "Error: Division by zero!"
    elif op == "**":
        answer = num1 ** num2
    else:
        answer = "Invalid operation!"

    print("Result:", answer)
    print("-------------------")

    again = input("Do you want to calculate again? (yes/no): ")
    if again == "no":
        print("Goodbye!")
        break