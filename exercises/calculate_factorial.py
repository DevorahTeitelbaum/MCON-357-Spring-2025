# implemented factorial_recursive method
def factorial_recursive(number):
    if number > 0:
        return number * factorial_recursive(number - 1)
    elif number == 0:
        return 1;
    else:
        if number.__floor__() is not number:
            print("Number is not an integer. cannot calculate")
        else:
            print("Number is negative. cannot calculate")

def main():
    print("Factorial Computation Using Recursion")
    errorMessage = "e"
    while errorMessage is not None:
        number = str(input("Enter a non-negative integer: "))
        number, errorMessage = handle_input(number)
        if errorMessage is not None:
            print(errorMessage)


    print("Factorial of " + str(int(number)) + " is: " + str(factorial_recursive(int(number))))

def handle_input(number):
    try:
        number = int(number)
        if number < 0:
            return None, "Number cannot be negative"
        else :
            return number, None
    except ValueError:
        return None, "Number must be an integer"

if __name__ == "__main__":
    main()
