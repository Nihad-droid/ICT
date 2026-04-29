import math
# numbers
num1 = float(input("Type your first number:\n"))
num2 = float(input("Type your second number:\n"))
# functions


def summation():
    print(str(float(num1)), "+", str(float(num2)), "=", num1+num2)


def subtraction():
    print(str(float(num1)), "-", str(float(num2)), "=", num1 - num2)


def multiplication():
    print(str(float(num1)), "*", str(float(num2)), "=", num1 * num2)


def division():
    print(str(float(num1)), "/", str(float(num2)), "=", num1 / num2)


def logarithm():
    print("Logarithm", str(num2), "base", str(num1), "=", math.log(num2, num1))


def exp():
    print(str(num1), "to the power of", str(num2), "equals to", num1 ** num2)


def factorial():
    n = int(input("Enter the number you want to find the factorial of\n"))
    starter = 1
    for i in range(1, n + 1):
        starter = starter * i
    print(starter)


# applying functions depending on the number
func = int(input("\nPress 1,2,3,4,5,6 or 7 to:\n1-add         2-subtract\n3-multiply    4-divide\n5-logarithm   6-exponentiate\n7-factorial\n"))
if func == 1:
    summation()
elif func == 2:
    subtraction()
elif func == 3:
    multiplication()
elif func == 4:
    try:
        division()
    except ZeroDivisionError:
        print("Can't divide by zero")
elif func == 5:
    try:
        logarithm()
    except ValueError:
        print("Value Error\n*Notes: 1)Make Sure that the base of a logarithm can`t be equal to neither 0 nor 1.\n        2)The value of a logarithm must be equal to positive number.")
elif func == 6:
    exp()
elif func == 7:
    factorial()
else:
    print("I can't help you with that request!")
