# PYTHON LISTS
"""
1. List: used to store multiple items in a single variable, created using square barckets []
2. List items
- ordered: order of list items are defined and that cannot change, new items placed at the end of the list
- changeable: items can be changed means add, remove after list creation
- allow duplicate values: items can be repeated
- indexed: items are indexed like 1st item = 0, 2nd item = 1 and so on
3. List length: no. of items in the list, len() function
4. List items - Data types
5. list type: type() function - <class 'list'>
6. list() constructor: new list creation using list()
"""
thislist = ["apple", "banana", "cherry"] # this is a list
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"] # list has duplicate values
print(thislist)
thislist = ["apple", "banana", "cherry"] # Length of the list 
print(len(thislist))
list1 = ["apple", "banana", "cherry"] # List data types
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
list4 = ["abc", 34, True, 40, "male"]
print(list4)
mylist = ["apple", "banana", "cherry"] # What is the data type of a list?
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets: List creation
print(thislist)
# Python collections (Arrays)
"""
1. List: ordered and changeable, allows duplicate members
2. Tuple: ordered and unchangeable, allows duplicate members
3. Set: unordered, unchangeable (add and remove items is possible), and unindexed, no duplicate members
4. Dictionary: ordered and changeable, no duplicate members
"""
# Access list items - list items are indexed, starts from 0,1,2 and so on.
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Print the second item of the list

# Negative indexing - starts from end, starts from -1,-2 and so on
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # Print the last item of the list

# Range of Indexes - range defined by start and end position or value, return value will be a new list with the specified items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Range of indexes
"""Note: The search will start at index 2 (included) and end at index 5 (not included)"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # By leaving out the start value, the range will start at the first item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # By leaving out the end value, the range will go on to the end of the list

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # returns the items from "orange" (-4) to, but NOT including "mango" (-1)

# Check if Item Exists - in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # Change the second item

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #Change the second value by replacing it with two new values
"""Note: The length of the list will change when the number of items 
inserted does not match the number of items replaced."""

# Insert Items - insert() method inserts an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # Insert "watermelon" as the third item
print(thislist)

# Python - Add List Items - append() method - adds items at the end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List -  extend()-append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable - using extend() method - can add any iterable object (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove List Items
# remove() method - Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # Remove Specified Item
print(thislist)

# pop() method - Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop() # Remove the last item
print(thislist)

# del keyword 

thislist = ["apple", "banana", "cherry"]
del thislist[0] # removes the specified index
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist # Delete the entire list

# Clear the List - clear() method - empties the list
# The list still remains, but it has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear() # Clear the list content
print(thislist)

# Loop Lists - for loop
thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x) # Print all items in the list, one by one

# Loop Through the Index Numbers : Use the range() and len() functions to create a suitable iterable
thislist = ["Orange", "banana", "cherry"]
for i in range(len(thislist)): #Print all items by referring to their index number
  print(thislist[i]) #The iterable created in the example above is [0, 1, 2]

# Using a While Loop
# 1. Use the len() function to determine the length of the list
# 2. Start at 0 and loop through the list items by referring to their indexes
# 3. Increase the index by 1 after each iteration
thislist = ["Mango", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension -  The shortest syntax for looping through lists
thislist = ["Lion", "Tiger", "Bear"]
[print(x) for x in thislist]

# PYTHON - LIST COMPREHENSION
# 1. Offers a shorter syntax when creating a new list based on the values of an existing list
# Example - Without using List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# Example - With using List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax - newlist = [expression for item in iterable if condition == True]
# The return value => new list, leaving the old list unchanged
# Condition => filter that only accepts the items that is "True"
# Example: newlist = [x for x in fruits if x != "apple"] 
list = ["Pear", "Carrot", "Banana", "Mango", "Apple", "Lime", "Watermelon", "Guava"]
newlist = [x for x in list if x!="Apple"]
print(newlist)
# Without if condition
list = ["Pear", "Carrot", "Banana", "Mango", "Apple", "Lime", "Watermelon", "Guava"]
newlist = [x for x in list]
print(newlist)

# Iterable - Using range() method to create an iterable
newlist = [x for x in range(10)]
print(newlist)
# With a condition
newlist = [x for x in range(10) if x < 5] # Accept only numbers lower than 5
print(newlist)

# Expression
# 1. Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
