import math

print("Calculator:")
print("(+) (-) (x) (/)")
print("(1) (2) (3)")
print("(4) (5) (6)")
print("(7) (8) (9)")
print("(0) (.) (=)")

keep_using = True

while keep_using:
    num_1 = input("First number: ")
    operator = input("Operator (+, -, x, /): ")
    num_2 = input("Second number: ")

    if operator == "+":
        result = int(num_1) + int(num_2)
    elif operator == "-":
        result = int(num_1) - int(num_2)
    elif operator == "x":
        result = int(num_1) * int(num_2)
    elif operator == "/":
        result = int(num_1) / int(num_2)

    print(num_1 + " " + operator + " " + num_2 + " = " + str(result))
    play_again = input("Would you like to use the calculator again? (y/n)")

    if play_again == "y":
        keep_using = True
    else:
        keep_using = False
