#!/usr/bin/env python3

# very simple calculator
# you choose one from the basic arithmetic operations 
# and provide two numbers, the script returns the result
# if you don't quit the script, it asks you the next operation you want to perform
# each operation handles only 2 parameters at the time

# the script contains some errors: if you run it, it will generate some exceptions
# you have to fix this script and try to improve it by using some of the tricks you learnt

# sum
def SUM(a, b):
    return a+b

# subtraction
def SUB(a, b):
    return a-b

# multiplication
def MUL(a, b):
    return a*b

# division
def DIV(a, b):
    return a/b

def print_menu():
    print("Press \"a\" for sum")
    print("Press \"b\" for subtraction")
    print("Press \"c\" for multiplication")
    print("Press \"d\" for division")
    print("Press \"e\" for exit")

# boolean value quit
quit = False

# while quit is False
while (not quit):
    print_menu()
    operation = input("Your choice: ")
    if (operation == "a"):
        a = input("a = ")
        b = input("b = ")
        print("{} + {} = {}".format(a, b, SUM(a, b)))
    elif (operation == "b"):
        a = input("a = ")
        b = input("b = ")
        print("{} - {} = {}".format(a, b, SUB(a, b)))
    elif (operation == "c"):
        a = input("a = ")
        b = input("b = ")
        print("{0} x {1} = {2}".format(a, b, MUL(a, b)))
    elif (operation == "d"):
        a = input("a = ")
        b = input("b = ")
        print("{0} : {1} = {2}".format(a, b, DIV(a, b)))
    elif (operation == "e"):
        quit = True
    else:
        print(operation, "is not a valid choice")
