# Strings

# Strings is data type that stores a sequence of characters

str1 = "This is a String."
str2 = 'Khanzadi'
str3 = """This is a String."""

# Single Code use String (use single code ')
"This is codeone's channel"
'This is codeone"s channel'

# Ager hamy code ko next line ma bhe run kern ho tu us ka liya
# (escape, sequence, characters ) in ka kam formating dena hota hain matlab tab spase and next line ka liya use kerty hain
# String normal print 
str1 = "This is a String. We are creating it in python."
print(str1)

# String nex line Print
# \n escape sequence character mean nex line
str1 = "This is a String.\nWe are creating it in python."
print(str1)

# \t tab sequence character mean nex line
str1 = "This is a String.\tWe are creating it in python."
print(str1)

# Basic Strings Operations 

# Concatenation  (2 string ko milana) use + operator
# "hello" + "world" -> "helloworld"
str1 = "Khanzadi"
str2 = "Memon"
print(str1+str2)
        # OR
str1 = "Khanzadi"
str2 = "Memon"
final_str = str1+str2
print(final_str)

# Find out String Length (Length of str)
# Python ma length len(str) ak function hta hy jo kise string ki ki length calculate kerta hy
# len(str) length ka ander spaces characters bhe add hoty hy or spical characters bhe use hoty hy 
str1 = "Khanzadi"
len1 =  len(str1)
print(len1)

str2 = "Memon"
len2 =  len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))

# Python ma string sa related ak or interesting chez hy jo Indexing hy
#  Indexing use in all programming lenguages
# jab bhe ak string create hoti hy tu internaly us ka sary characters ko ak index mil jata hy
# index is kind of saying us character ko apni ak position number mil jati hy 