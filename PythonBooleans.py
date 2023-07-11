# PYTHON BOOLEANS - Two Values: True or False
print(10 > 9) # Example
print(10 == 9) # Example
print(10 < 9) # Example
a = 200 # Example
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# EVALUATE VALUES and VARIABLES - bool() function - Allows to evaluate any value and return 'True' or "False'
print(bool("Hello")) # Evaluate a STRING
print(bool(15)) # Evaluate a Value
# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
# Examples for TRUE values
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
"""
Only few returns 'FALSE':
Empty values such as (), [], {}, ""
The number 0
The value None
The value False evaluates to False
"""
# Examples for FALSE values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# Returns FALSE if an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
# Functions can Return a Boolean
def myFunction():
  return True
print(myFunction())  # Print the answer of a function:
# Example: Execute code based on the Boolean answer of a function:
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!") #Print "YES!" if the function returns True, otherwise print "NO!"
# Built-in functions that return a boolean value - isinstance() function
x = 200
y = 100
print(isinstance(x, int)) # Check if an object is an integer or not
print(isinstance(y, str))