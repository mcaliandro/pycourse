#!/usr/bin/env python3

### Functions and Lambdas

# define the myprint() function that requires two parameters as input
# one is mandatory (msg) that cannot be empty
# one is optional (greeting) because it is set to a default value

# please note that in Python the indentation is very important
# you shoud use the tab (or 4 spaces) to specify a inner block of code

# in languages like C++, the block is specified within the braces { and }
# like this:

# void myfunction() {
#     // inner block
# }

# the following example uses indentation for the body of the function
# and for the body of the if-statement
# to close a block, just return at the previous indentation "level"

def myprint(msg, greeting=True):    
    # you can use escape characters within a string to format it
    print("\n~~~~~~~~~~")   # using \n (newline)
    
    if greeting:
        # concatenation of two strings with + operator
        msg = "Hello, " + msg
    # if-statement is now closed
    
    print("\t", msg)    # using \t (tab)
    print("~~~~~~~~~~")
# myprint is now closed

# pass only name as parameter and use greeting's default value
name = "World"
myprint(name)

# specify that greeting should be set to False
myprint(name, greeting=False)


# of course, functions can return a value
def my_name_is():
    return "William"

print("Hello,", my_name_is())

# or more values
def my_lucky_numbers():
    return 1, 3

n1, n2 = my_lucky_numbers()
print("My lucky numbers are {} and {}".format(n1, n2))


## Lambdas
# they are anonymous functions, e.g., use them only once and then throw
# the scope is to use them "locally" and not "globally", i.e.
# - define a function within another function and don't allow others to access/use them

# sq_area lambda takes one parameter
sq_area = lambda side: side * side

# tr_area lambda takes two parameters
tr_area = lambda base, height: (base * height) / 2

print("Square area with side=3 is", sq_area(3))
print("Square area with side=8 is", sq_area(8))
print("Trangle area with base=3 and height=4 is", tr_area(3, 4))
print("Trangle area with base=2 and height=5 is", tr_area(3, 4))

# now they are not functions anymore
sq_area = 3 * 3
print("Square area with side=3 is", sq_area)
tr_area = 3 * 4
print("Trangle area with base=3 and height=4 is", tr_area)


# NOTE: remember that there are functions like print() which are built-in functions 
#       provided by the Python interpreter, that means if you write your own 
#       implementation within a script, you are overriding their behaviors
#       this is true when you redefine the function within a script or in a 
#       Python's console enviroment, so you are not changing the behavior forever
#       because Python allows you to do so, but it's convenient to use a different
#       name in case you want to preserve the original behavior

# here, we are going to redefine the behavior of print()
# now it works only with two parameters p1 and p2


def print(p1, p2):
    return str(p1) + str(p2)

# NOTE: please notice the new definition of print()
#       now it takes two parameter, converts them into strings and concatenates
#       them into a new one which is returned as a value

# type casting := converting a value from a data type to another (if admissible)

a = "January"
b = 1999

# use print() according its new behavior
print(a, b)

help_message = """Python has lost the original behavior of the print() function. 
It was better to define the new behavior by using a different name,
as we did previously with myprint() function"""

# NOTE: now the Python interpreter is not able anymore to print the content in output
#       fortunately, this is true only within this script
# Plese rembember to choose the name of your functions wisely

print(help_message)
