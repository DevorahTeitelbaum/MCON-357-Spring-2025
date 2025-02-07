# implemented factorial_recursive method
def factorial_recursive(number):
    if number > 0:
        return number * factorial_recursive(number-1)
    elif number == 0:
        return 1;

def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # handle negative input
    while number < 0:
        number = int(input("Only positive values allowed. Enter a non-negative integer: "))

    # Call factorial_recursive method in the printline as answer
    print("Factorial of " + str(number) + " is: " + str(factorial_recursive(number)))

if __name__ == "__main__":
    main()
