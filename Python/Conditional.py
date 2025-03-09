#Conditional Statements
#if-elif-else (Syntax)

"""if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN"""

#Traffic Light Code

light = input("light color: ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#Grades of students

marks = input("marks: ")
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")
