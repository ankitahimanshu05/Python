# PYTHON - SLICING STRINGS
"""
For returning range of characters - by using slice syntax
Specify the start and end indices, separated by colon, to return the part of the string
"""
# Examples
b = "Learning is fun!"
print(b[2:7]) # from character position 2 to 6 (7 not included)
b = "Learning is fun!"
print(b[:7]) # from start to 6 (7 not included)
b = "Learning is fun!"
print(b[2:]) # from 2 to end
# NEGATIVE INDEXING - start slicing from end of the string
b = "Hello  World!"
print(b[-5:-2]) # from "o" in World! (position -5) to but not included "d" in "World!" (position -2)