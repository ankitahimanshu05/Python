# Build-in Data types
"""
Text type - str
Numeric type - int, float, complex
Sequence type - list, tuple, range
Mapping type - dict
Set type - set, frozenset
Boolean type - bool
Binary type - bytes, bytearray, memoryview
None type - NoneType
"""
# Examples for different DATA TYPES
a = "Hello World"
b = 20
c = 20.5
d = 1j
e = ["Apple", "Banana", "Cherry"]
f = ("Pear", "Watermelon", "Papaya")
g = range(6)
h = {"name":"John", "Age":36}
i = {"Lion", "Tiger", "Bear"}
j = frozenset({"Alpha", "Beta", "Gamma"})
k = True
l = b"Hello"
m = bytearray(5)
n = memoryview(bytes(5))
o = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
# Setting the Specific Data Type - to specify the data type, one can use the following CONSTRUCTOR functions
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)	
x = list(("apple", "banana", "cherry"))	
x = tuple(("apple", "banana", "cherry"))	
x = range(6)	
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)
x = bytes(5)
x = bytearray(5)	
x = memoryview(bytes(5))