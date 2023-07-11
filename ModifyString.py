# PYTHON - MODIFY STRINGS
"""
Uppercase - upper(): returns in UPPERCASE
Lowercase - lower(): returns in LOWERCASE
Remove whitespaces - strip(): removes whitespaces from the beginning or the end
Replace - replace(" "," "): replaces a string with another
Split - split(): returs a list where separators are found 
"""
# Examples
a = "Hello, World!"
print(a.upper()) # returns HELLO, WORLD!
a = "Hello, World!"
print(a.lower()) # retuens hello, world!
a = " Hello, World! "
print(a.strip()) # returns Hello, World!
a = "Hello, World!"
print(a.replace("H", "J")) # returns Jello, World!
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']