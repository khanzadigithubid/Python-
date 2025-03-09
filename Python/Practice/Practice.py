# Write a program to 2 numbers and print their sum.
first = int(input("enter first:"))
second = int(input("enter second:"))

print("sum = ", first + second)


#WAP to input side of a square and print its area.
side = float(input("enter square side :"))

print("area =", side * side)

side = float(input("enter square side :"))

print("area =", side ** 4)


#WAP to input 2 floating point numbers and print their average.
a = float(input("enter first: "))
b = float(input("enter second: "))

print("avg = ", (a + b) /22)

# WAP to input 2 int numbers, a and b
# Print True if a is grater than or equal to b. If not print False.
a = float(input("enter first: "))
b = float(input("enter second: "))

print(a >= b)

#State True and False
#1) /* is a symbol used in python for single line comment.    False
#2) 2ndNAme s an invalid identifier in python.  True
#3) ** is a valid arithmetic operator in python.  True
#4) in is a logical operator in python.      False
#5) Variable declaration is implicit in python.   True
#6) Consider the given expression: not True and False o True
# which of the following will be correct output if he given expression is evaluated?
# (not True) and False or True
# False 
# (False and False) or True
#False
#(False or True)
# True
#Final answer True

#Print outfit for:
#A = 5 & G = M   (fee is 300)
#A = 2 & G = F    (fee is 200)

A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif((A == 3 or A == 4) and G == "F"):
        print("fee is 200")
elif(A == 5 or G == "M"):
      print("fee is 300")
else:
      print("no fee")

