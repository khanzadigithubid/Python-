# Expression Execution

# String & numeric values can operate together with *
#ager string ko number sa multiple kay gy tu utni hi time string ma answer ay ga
# A,B=2,3
#Text="@"
#print(2*Text*3) // @@@@@@

# String & String can operate with + 2@  (technical terms ma concatenation bolty hain q ka string or string + ka zary sath milty hain)
#A,B="2",3
#Text="@"
#print((A+Text)*B)  // 2@2@2@

# Numeric values can operate with all arithmetic operators
#A,B=2,3
#C=4
#print(A+B*C) //14

# Arithmetic expression with integer and float will result in float.
#A,B=10,5.0
#C=A*B
#print(C) //50.0

# Result of division operator with two integers will be float.
#A,B=1,2
#C=A/B
#print(C)  //0.5

# Integer division with float and int will give int displayed as float.
# Integer division (//) (roundoff ker ka value ko integer ma convert kerta hy round off ker ka choty integer ma convert kerta hy)
# A,B=1.5,3
#C=A//B
#print(C, A/B)  //0.0     //0.5

# Floor gives closer integer, which is lesser than or equal to the float value 
# Result of (A//B) is same as floor (A/B)
# Floor ak function hota hy maths ka ander jis ka matlb hota hy
# floor koager ham kohe number dy gy tu us ka clooser integer number nikly ga (equal value ho ya baraber jo)

# A,B=12,5
#C=A//B
#print(C)  //2

# A,B=-12,5
#C=A//B
#print(C)  //-3

# A,B=12,-5
#C=A//B
#print(C)  //-3

# Remainder is negative when denominator is negative 
# Numenator, Denominator
# +,+=+ 
# -,-=+
# +,-=-
# -,+=+

# A,B=-5,2
#C=A%B
#print(C)  //1

# A,B=5,2
#C=A%B
#print(C)  //1

# A,B=5,-2
#C=A%B
#print(C)  //-1