# Type Conversion (vo hoti hy jis mai ak variable ko dosry variable mai convert kerty hain yani integer type ko float type ma converst ka liya conversion use kerty hain)
#two type of conversion
# 1) Type Conversion (automatically type convert kerta hain python )
# 2) Type Casting (manually (zabardasti) type convert kerna)
# float ka ander zyada data store hta hain  ka ya decemail values hoti hain point mai (ponit(.) exttra information ko dekhata hain)

# 1) Type Conversion (automatically type convert kerta hain python )
"""Type conversion occurs when one variable is converted into another variable type. For example, converting an integer type to a float type requires type conversion.

Two Types of Conversion:
Type Conversion – Python automatically converts one data type to another.
Type Casting – Manually (forcefully) converting one data type to another.
A float type can store more data because it includes decimal values. The point (.) represents extra information in floating-point numbers.

1) Type Conversion
Python automatically converts data types as needed."""
a = 40 #integer
b = 30.5 #float

#integer convert in float(superior value)

sum = a + b
print(sum)

# string ko floating value ma convert ni ker sakhty  ka pythn error dy gi q ka string ko string ma kary gy

# 2) Type Casting (manually (zabardasti) type convert kerna)
# valid number hoga tab hi type casting work kary gi
"""A string cannot be converted into a floating value, as Python will give an error because a string remains a string.
2) Type Casting (manually forcing type conversion)
Type casting will only work if the value is a valid number."""
a = int("6")
b= 5.25

print(type(a))
print(a + b)

a = float("6")
b= 5.25

print(type(a))
print(a + b)

a = 25.65
a = str(a)

print(type(a))