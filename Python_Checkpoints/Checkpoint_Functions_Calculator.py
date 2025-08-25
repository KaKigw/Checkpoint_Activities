def Calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero error"

    return {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

def main():
    operations= Calculator()
    print("Welcome to the Calculator!")
    while True:
        op = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if op == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if op not in operations:
            print("Invalid operation. Please try again.")
            continue
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = operations[op](x, y)
            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

main()