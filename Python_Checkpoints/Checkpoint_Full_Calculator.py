
""" Create a class called "Calculator" that contains the following:
A dictionary attribute to store the available mathematical operations and their corresponding functions
A method called "init" that initializes the dictionary with the basic mathematical operations (+, -, *, /) and corresponding functions
A method called "add_operation" that takes in two arguments: the operation symbol and the corresponding function. This method should add the new operation and function to the dictionary.
A method called "calculate" that takes in three arguments: the first number, the operation symbol, and the second number. This method should use the dictionary to determine the appropriate function to perform the calculation. It should also include error handling to check if the operation symbol is valid and if the input values are numbers. If an error is encountered, the method should print an error message and raise an exception.
Create separate functions for the advanced mathematical operations (exponentiation, square root, logarithm) and use the "add_operation" method to add them to the calculator's dictionary.
In the main program, create an instance of the Calculator class, and use a while loop that allows the user to continue performing calculations until they choose to exit.
Use the input() function to get input from the user for the numbers and operation symbol.Use the math library for advanced mathematical operations
Use the isinstance() function to check if the input is a number. """

import math as m 

class Calculator:
    def __init__(self): #
        self.operation = {
            "+" : lambda x,y: x+y,
            "-" : lambda x,y: x-y,
            "*" : lambda x,y: x*y,
            "/" : self.Safe_Division
        }
    
    #Verify if the division is possible
    def Safe_Division(self,x,y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x/y
    
    def add_operation(self,symbol:str,Function):
        self.operation[symbol] = Function
    
    def calculate(self,x,symbol,y=None):
        #Validate Inputs
        if not isinstance(x, (int, float)):
            raise TypeError("First input must be a number")
        if y is not None and not isinstance(y, (int, float)):
            raise TypeError("Second input must be a number")

        
        #Validate if the operation exist
        if symbol not in self.operation:
            raise ValueError("The Operation doesn't exist")
        
        #Verify if its Unary or Binary
        Func = self.operation[symbol]

        try:
            return Func(x) if y is None else Func(x, y)
        except Exception as e:
            raise RuntimeError(f"Error during '{symbol}' calculation: {e}")
            

calc = Calculator()
calc.add_operation('^', lambda a, b: m.pow(a, b))
calc.add_operation('sqrt', lambda a: m.sqrt(a) if a >= 0 else (_ for _ in ()).throw(ValueError("Cannot take square root of a negative number")))
calc.add_operation('log', lambda a: m.log(a) if x <= 0 else (_ for _ in ()).throw(ValueError("Logarithm undefined for zero or negative numbers.")))

print("🔢 Welcome to the Python Calculator!")
print("Available operations: +, -, *, /, ^, sqrt, log")

while True:
    op = input("\nEnter operation symbol (or 'exit' to quit): ").strip()
    if op.lower() == 'exit':
        print("GoodBye")
        break
    if op in ['sqrt', 'log']:
        x = float(input("Enter the number: "))
        result = calc.calculate(x, op)
    else:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = calc.calculate(x, op, y)
        
    print(f"The result is:{result}")
