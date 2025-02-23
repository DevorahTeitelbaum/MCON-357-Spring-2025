import sys


# implemented factorial_recursive method
def factorial_recursive(number):
    if number >= 1:
        return number * factorial_recursive(number-1)
    #base case, number == 0
    else:
        return 1


# implemented factorial_iterative method
def factorial_iterative(number):
    total = 1
    for i in range(number + 1):
        if i > 0:
            total = total * i
    return total


# main method to run factorial methods
def main():
    print("Factorial Computation Using Recursion")
    errorMessage = "e"
    while errorMessage is not None:
        number = input("Enter a non-negative integer: ")
        number, errorMessage = handle_input(number)
        if errorMessage is not None:
            print(errorMessage)
    if number >= sys.getrecursionlimit():
        print(f"Factorial of {number} is {factorial_recursive(number)}")
    else:
        print(f"Factorial of {number} is {factorial_iterative(number)}")


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
