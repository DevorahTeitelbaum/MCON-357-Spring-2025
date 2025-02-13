# implemented factorial_recursive method
def factorial_recursive(number):
    # handle negative input
    while number < 0:
        number = int(input("Only positive values allowed. Enter a non-negative integer: "))
    if number > 0:
        return number * factorial_recursive(number - 1)
    elif number == 0:
        return 1;


def main():
    print("Factorial Computation Using Recursion")
    isBadInput = True
    number = .5
    while isBadInput:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                isBadInput = False
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


    print("Factorial of " + str(number) + " is: " + str(factorial_recursive(number)))


if __name__ == "__main__":
    main()
