# PYTHON STRINGS - surrounded by single or double quotation marks
"""
'HELLO' is same as "HELLO"
Can be displayed by using print() function
"""
# Example
print("Hello")
print('Hello')
# Assigning string to a variable
a = "Python"
print(a)
# Multiline strings - by using three quotes (""") or (''')
a = """Python 
is a
programming language"""
print(a)
"""
Strings, in Python, are ARRAYS of bytes representing unicode characters
In PYTHON, no CHARACTER DATA TYPE, a Single character is string with a length of 1
Sqaure brackets[]-used to access elements of the string
"""
# To get a character at position 1
a = "Hello Python"
print(a[1]) # First character has position 0
# LOOPING through a string - Using for loop
for x in "Banana":
   print(x)
# STRING LENGTH - Using len() function
a = "HELLO WORLD!"
print(len(a))
# CHECK STRING = to check a certain phrase/character is present in a string - Two ways
# Using 'in' keyword
txt = "The best things in life are free."
print("free" in txt)
# Using 'if' statement
txt = "The best things in life are free."
if "free" in txt:
   print("Yes, 'free' is present.")
# CHECK if NOT present in STRING
# Using 'not in' keyword
txt = "the best things in life are free!"
print("expensive" not in txt)
# Using 'if' statement
txt = "the best things in life are free!"
if "expensive" not in  txt:
   print("No, 'expensive' is NOT present.")