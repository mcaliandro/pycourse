#!/usr/bin/env python3


## Numeric variables

# these are numeric variables
x = 5       # integer
y = 0.123   # float
z = 5j      # complex (put the j after the real part)

# print is a built-in function that show some values in output
print("x is an integer number:", x)
print("y is a float number:", y)

# in case you have to print multiple values in output, you can use the format()
# function on a string. you should use some placeholders {n} in the string to specify
# where to put the values, you can order them by specifying the position that 
# corresponds to the order of values reported inside format(), the position starts from 0
# in this case, z.real goes to position 0, z.imag in position 1
print("z is a complex number, Real: {0}, Imag: {1}".format(z.real, z.imag))

# if you don't specify any position, the function will put the values 
# in the order specified in foramat()
print("z is a complex number, Real: {}, Imag: {}".format(z.real, z.imag))


## Boolean variables
a = True
b = False

print("a={}, b={}", format(a, b))
print("a AND b = ", (a and b))
print("a OR b = ", (a or b))
print("a AND (not b)", (a and (not b)))


## String variables

name = ""           # empty string
greeting = "Hello," # initialized string

# print both variables in output
print(greeting, name)

# the function input() reads some values from input (keyboard)
# if you pass a string as parameter to input(), the function
# will show that message for asking the user to provide the value
name = input("Your name:")
print(greeting, name)
 

# NOTE: a variable is not constrained to store only one data type
#       in C++ or Java, once a variable has been defined as int,
#       it will store only integer values, otherwise an error occurs
#       instead Python provides more flexibility
 

# here, the variable name has been defined has string
# now, it becomes an integer value
name = 243

# print both variables in output
print(greeting, name)
