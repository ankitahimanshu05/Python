# PYTHON CASTING - Specify a variable type
""" 
int()-construct an integer number from integer, float (by removing decimals) or string (has a whole number as string)
float()-contructs a float number from integer, float or string (has a float or interger as string)
str()-construct a string from wide variety of data types including string, integer or float
"""
# Example for int()
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x, y, z)
# Example for float()
a = float(1)     # x will be 1.0
b = float(2.8)   # y will be 2.8
c = float("3")   # z will be 3.0
d = float("4.2") # w will be 4.2
print(a, b, c, d)
# Example for string()
p = str("s1") # x will be 's1'
q = str(2)    # y will be '2'
r = str(3.0)  # z will be '3.0'
print(p, q, r)