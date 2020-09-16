#!/usr/bin/env python3

# you provide a sequence of numbers, the script stores them into a list
# if you don't quit the script, it asks you the next number

# import is as way to use external modules within the script
import random

# this is an empty list
numbers = []

print("Press \"q\" for quit\n")

quit = False
while (not quit):
    value = input("Insert a number: ")
    if value == "q":
        quit = True
    else:
        # try-except is useful to manage runtime errors
        try:
            # an exception can be raisen in case an error occurs during the casting
            
            # convert a string to int
            value = int(value)
            
            # if the casting from string to integer generates an error
            # i.e., the value string contains some non-digit characters 
            # the executions jumps to the exception handling section (except)
            # and the following instructions are not executed
            
            # add new value to numbers
            numbers.append(value)
            
        except ValueError:
            # handle the exception ValueError here 
            print(value, "is not a number\n")


# show info about numbers list

# you can just pass the list to the print function to show its content
print("\nPrint the elements within the list:", numbers)

# use the len() function to get the dimension of the list
print("\nNumber of elements within the list:", len(numbers))

# use the sum() function to get the sum of the numbers list
print("\nSum of the numbers within the list:", sum(numbers))

# a way to get a random item within the list is to generate a random index
# fetch it within the range [0, N), where N := len(numbers)
i = random.randint(0, len(numbers))

# access the element through its index: list[index]
print("Picking up a random element from the list:", numbers[i])

# NOTE: remember that functions like print(), sum(), len() are directly provided by python
#       that mean if you write your version of them in a script, (with some probability) 
#       you won't get the original result
