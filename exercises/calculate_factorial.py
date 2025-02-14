# implemented factorial_recursive method
import sys

# implemented factorial_recursive method
def factorial_recursive(number):
    if number > 2:
        return (number * (number - 1)) * factorial_recursive(number - 2)
    elif number == 2:
        return 2
    elif number == 1:
        return number * factorial_recursive(number - 1)
    elif number == 0:
        return 1
    else:
        if number.__floor__() is not number:
            print("Number is not an integer. cannot calculate")
        else:
            print("Number is negative. cannot calculate")


# implemented factorial_iterative method
def factorial_iterative(number):
    if number >= 0:
        total = 1
        for i in range(number + 1):
            if i > 0:
                total = total * i
        return total
    else:
        if number.__floor__() is not number:
            print("Number is not an integer. cannot calculate")
        else:
            print("Number is negative. cannot calculate")


# main method to run factorial methods
def main():
    print("Factorial Computation Using Recursion")
    errorMessage = "e"
    while errorMessage is not None:
        number = str(input("Enter a non-negative integer: "))
        number, errorMessage = handle_input(number)
        if errorMessage is not None:
            print(errorMessage)
    print("Factorial of " + str(int(number)) + " is: " + str(factorial_recursive(int(number))))


# input handler to ensure only applicable numbers enter the factorial methods
def handle_input(number):
    try:
        number = int(number)
        if number < 0:
            return None, "Number cannot be negative"
        else:
            return number, None
    except ValueError:
        return None, "Number must be an integer"


if __name__ == "__main__":
    main()
