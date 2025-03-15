# Best Practices

# 1.Simple instructions
# 2.One instruction per task
# 3.Short & meaningful variable names
# 4.Use appropriate comments
# 5.avoid complex expressions

# Calculate the Simple Interest 
# P = Principal Amount
# R = Rate of Interest
# T = Time Period

# ST = P*R*T/100

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
print(a*b*c/100)

# Improved Code

p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (p*r*t)/100
print(si)
