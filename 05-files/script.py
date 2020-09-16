#!/usr/bin/env python3

# the script generates a sequence of random numbers and then stores them into a file
# to double check the result, it reads the file and prints the content

# in Python you can just import the components of the module you need
from random import randint


fname = "numbers.txt"

# this feature of Python is called list comprehension
# range(1000) returns a list of integers within [0, 1000] range
numbers = [randint(0, 20) for i in range(1000)]
print("Numbers: ", numbers)

# write the numbers list into a file
f = open(fname, "w")
for n in numbers:
    f.write(str(n) + "\n") # convert the number n to a string
f.close()

# read the file content
with open(fname, "r") as f:
    for line in f:
        line = line.rstrip('\n') # rstrip to remove the newline char
        print(line)
# by using <with> you don't need to call close() at the end
