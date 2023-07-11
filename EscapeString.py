# PYTHON ESCAPE CHARACTER
"""
Used to INSERT illegal character in a string
Backslash (\) with a character to insert
Example: txt = "We are the so-called "Vikings" from the north." - ERROR
"""
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# OTHER ESCAPE CHARACTERS:
# \'	Single Quote
txt = 'It\'s alright.'
print(txt) 	
# \\	Backslash	
txt = "This will insert one \\ (backslash)."
print(txt) 
# \n	New Line	
txt = "Hello\nWorld!"
print(txt) 
# \r	Carriage Return
txt = "Name Ankita!"
print(txt) 	
# \t	Tab
txt = "Hello\tWorld!"
print(txt) 
# \b	Backspace - This example erases one character (backspace):
txt = "Hello \bPython!"
print(txt) 	
# \f	Form Feed	
# \ooo	Octal value - A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
# \xhh	Hex value - A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)