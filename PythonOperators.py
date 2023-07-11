# PYTHON OPERATORS
"""
ARITHMATIC operators
# +	Addition	(x + y) adds two operands
# -	Subtraction	(x - y) subtracts two operands
# *	Multiplication	(x * y) multiplies two operands
# /	Division	(x / y) (float-QUOTIENT is always Float value) divides the first operand by the second
# %	Modulus (x % y) returns the remainder when the first operand is divided by the second
# **	Exponentiation	(x ** y) returns first raised to power second
# //	Floor division	(x // y) (floor-quotient returned by this operator is dependent on the argument being passed) 
      divides the first operand by the second
ASSIGNMENT operators
# =  x = 5	x = 5	Assign the value of the right side of the expression to the left side operand 
# +=	x += 3 same as x = x + 3 Add AND: Add right-side operand with left-side operand and then assign to left operand
# -=	x -= 3 same as	x = x - 3 Subtract AND: Subtract right operand from left operand and then assign to left operand
# *=	x *= 3 same as	x = x * 3 Multiply AND: Multiply right operand with left operand and then assign to left operand
# /=	x /= 3 same as	x = x / 3 Divide AND: Divide left operand with right operand and then assign to left operand
# %=	x %= 3 same as x = x % 3 Modulus AND: Takes modulus using left and right operands and assign the result to left operand
# //=	x //= 3 same as x = x // 3	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand
# **=	x **= 3 same as x = x ** 3	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand
# &=	x &= 3 same as	x = x & 3 Performs Bitwise AND on operands and assign value to left operand
# |=	x |= 3 same as	x = x | 3 Performs Bitwise OR on operands and assign value to left operand
# ^=	x ^= 3 same as x = x ^ 3 Performs Bitwise xOR on operands and assign value to left operand
# >>=	x >>= 3 same as x = x >> 3	Performs Bitwise right shift on operands and assign value to left operand
# <<=	x <<= 3 same as x = x << 3 Performs Bitwise left shift on operands and assign value to left operand
COMPARISON operators
# ==	Equal	(x == y)
# !=	Not equal (x != y)
# >	Greater than (x > y)
# <	Less than (x < y)
# >=	Greater than or equal to (x >= y)	
# <=	Less than or equal to (x <= y)
LOGICAL operators
# and: Returns True if both statements are true	(x < 5 and  x < 10)
# or: Returns True if one of the statements is true (x < 5 or x < 4)
# not: Reverse the result, returns False if the result is true	not (x < 5 and x < 10)
IDENTITY operators
# is: Returns True if both variables are the same object	(x is y)	
# is not: Returns True if both variables are not the same object (x is not y)
MEMBERSHIP operators
# in: Returns True if a sequence with the specified value is present in the object (x in y)
# not in: Returns True if a sequence with the specified value is not present in the object (x not in y)
BITWISE operators
# &: AND-Sets each bit to 1 if both bits are 1 (x & y)
# |: OR-Sets each bit to 1 if one of two bits is 1	(x | y)	
# ^: XOR-Sets each bit to 1 if only one of two bits is 1	(x ^ y()	
# ~: NOT-Inverts all the bits	(~x)
# <<: Zero fill left shift-Shift left by pushing zeros in from the right and let the leftmost bits fall off	(x << 2)	
# >>: Signed right shift-Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	(x >> 2)
"""
# EXAMPLES for all OPERATORS
x = 5
y = 3
print(x + y)
x = 5
y = 3
print(x - y)
x = 5
y = 3
print(x * y)
x = 5
y = 3
print(x / y)
x = 5
y = 3
print(x % y)
x = 5
y = 3
print(x ** y)
x = 5
y = 3
print(x // y)
x = 5
print(x)
x = 5
x+=5
print(x)
x = 5
x-=5
print(x)
x = 5
x*=5
print(x)
x = 5
x/=5
print(x)
x = 5
x%=5
print(x)
x = 5
x//=5
print(x)
x = 5
x**=5
print(x)
x = 5
x&=5
print(x)
x = 5
x|=5
print(x)
# EXAMPLES for BITWISE OPERATORS
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(6 & 3)
print(~3)
print(3 << 2)
print(8 >> 2)
# OPERATOR PRECEDENCE
"""
(): Parentheses	
**: Exponentiation	
+x  -x  ~x: Unary plus, unary minus, and bitwise NOT	
*  /  //  %: Multiplication, division, floor division, and modulus	
+  -:	Addition and subtraction	
<<  >>:	Bitwise left and right shifts	
&:	Bitwise AND	
^:	Bitwise XOR	
|:	Bitwise OR	
==  !=  >  >=  <  <=: is  is not  in  not in 	Comparisons, identity, and membership operators	
not:	Logical NOT	
and:	AND	
or:	OR
"""