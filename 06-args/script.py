#!/usr/bin/env python3

# this script uses some parameters (provided in input to the script)
# in order to perform some operations
# in a console, you can launch the script in this way:
#     script.py -o <arg> -f <arg>
# read the code and try to understand the scope of the parameters

import argparse

# in Python, a function called main is simply a function
# no special behaviors like C, C++ or Java
def main(op, fname):
    numbers = []
    try:
        f = open(fname, "r")
        numbers = [int(line.rstrip('\n')) for line in f]
    except:
        # no particular exception is specified
        print("An error occurred while accessing the file", fname)
    finally:
        # after having handled the error, just close the file 
        f.close()

    # check if list is not empty
    if numbers:
        if op == "sum":
            print("Sum: ", sum(numbers))
        elif op == "avg":
            print("Average: ", sum(numbers)/len(numbers))
        else:
            print("Invalid operation", op)
    else:
        print("Nothing happened: the list is empty")

# use ArgumentParser
parser = argparse.ArgumentParser(description="Calculate average and sum of a list of numbers within a file")

# add arguments -o and -f
parser.add_argument("-o", dest="op", required=True, help="Syntax: -o [avg|sum]")
parser.add_argument("-f", dest="fname", required=True, help="Synax: -f [filename]")

# parse the arguments
args = parser.parse_args()

# call main function
main(args)
