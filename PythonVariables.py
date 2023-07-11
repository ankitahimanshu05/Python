# PYTHON VARIABLES - Data Types
"""
Containers for storing data values
Created as the value is assigned
No command to declare any variable
"""
x = 5
y = "John"
print(x) 
print(y)
x = 4 # x is an Integer
print(x)
x = "Sally" # x is a String
print(x)
# Variable Casting - specifying data type of a variable
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x, y, z)
# Get the type of data - type() function
x = 5
y = "Peter"
print(type(x)) # Integer int
print(type(y)) # String Str
# Single or Double Quotes
x = "Sara"
# is same as 
x = 'Sara'
# Variable names are Case-sensitive
a = 4
A = "Parker"
# A will NOT overwrite a
# Rules for VARIABLE NAMES
"""
START with a LETTER or a UNDERSCORE 
CANNOT START with a NUMBER
CAN ONLY contain ALPHANUMERIC CHARACTERS and UNDERSCORE (A-z, 0-9 and _)
are CASE-SENSITIVE
CANNOT be any type of PYTHON KEYWORDS
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Illegal Variable Names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""
# Multi words Variable Names
"""
1 Camel Case - Each word, except the FIRST, starts with a CAPITAL letter
2 Pascal Case - Each word starts with a CAPITAL letter
3 Snake Case - Each word separated by an UNDERSCORE
"""
myVariableName = "Maria"
print(myVariableName)
MyVariableName = "Martha"
print(MyVariableName)
my_variable_name = "Mary"
print(my_variable_name)
# Assign Multiple Values to multiple VARIABLES in SINGLE line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Assign One value to multiple VARIABLES in SINGLE line
x = y = z = "Mango"
print(x)
print(y)
print(z)
# Unpack a collection - Extract values into variable
fruits = ["Apple", "Watermelon", "Papaya"] # Data type = 'list' type
x, y, z = fruits
print(x)
print(y)
print(z)

# PYTHON - OUTPUT VARIABLES - print() function
x = "Python is a programming language"
print(x)
# OR OUTPUT multiple variables separated by COMMA
x = "Python"
y = "is"
z = "great"
print(x, y, z)
# OR Use '+' operator to output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# For NUMBERS '+' sign works as mathematical operator
x = 5
y = 10
print(x + y)
# SRTING + NUMBER = ERROR
"""
x = 5
y = "Kevin"
print(x + y) # gives an error
"""
# Solution - Use COMMAS to print different data types
x = 5
y = "Kevin"
print(x, y)
# PYTHON - GLOBAL VARIABLES - def myfunc() function
"""
Variables created outside of a function
Can be used by everyone, both inside and outside of function
"""
x = "Power"
def myfunc():
   print("Knowledge is " + x)
myfunc()
# Creating variable with same name inside a function, Variable will be LOCAL and can only be used inside the function
# Global variable remains same as it was and with the ORIGINAL value
x = "awesome" # GLOBAL variable
def myfunc():
   x = "fantastic" # LOCAL variable
   print("Python is " + x) # Will take x as LOCAL
myfunc()
print("Python is " + x) # Will take x as GLOBAL
# Use of 'GLOBAL' keyword
def myfunc():
   global x # x is defined as GLOBAL variable
   x = "fantastic"
myfunc()
print("Python is " + x) # Hence can be used outside the function
# Use Global keyword to change a global variable inside a function
x = "awesome" # GLOBAL variable
def myfunc():
   global x
   x = "great" 
myfunc()
print("Python is " + x) # Value of x changed from 'awesome' to 'great' and is used as Global