#!/usr/bin/env python3

class Calculator:
    def __init__(self):
        self.operations = {
            "+": (lambda x,y: "{} + {} = {}".format(x, y, x+y)),  # sum
            "-": (lambda x,y: "{} - {} = {}".format(x, y, x-y)),  # subtraction
            "x": (lambda x,y: "{} x {} = {}".format(x, y, x*y)),  # multiplication
            ":": (lambda x,y: "{} : {} = {}".format(x, y, x/y))   # division
        }
    
    def __call__(self, choice, val1, val2):
        if choice in self.operations:
            return self.operations.get(choice)(val1, val2)
        else:
            return "Invalid operation {}".format(choice)
    
    def __str__(self):
        return "\nPress \"+\" for sum\nPress \"-\" for subtraction\nPress \"x\" for multiplication\nPress \":\" for division"


quit = False
calc = Calculator()

while not quit:
    print(calc)
    print("Press \"q\" for exit\n")
    op = input("Your choice: ")
    
    if op == "q":
        quit = True
        print("Exit")
    elif op in calc.operations:
        a = input("a is equal to: ")
        b = input("b is equal to: ")
        try:
            a = int(a)
            b = int(b)
        except:
            print("You've inserted an invalid number!")
        else:
            print(calc(op, a, b))
    else:
        print("Invalid operation", op)
