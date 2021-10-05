print("Hello world!")
#commente
print("""
multiple string 
pour le code editor 
""")

# Quick Math
print(" 50 + 50 ")
print(" 50 - 50 ")
print(" 50 * 50 ")
print(" 50 / 50 ")
print(" 50 ** 50 ") # Expponents
print(" 50 // 50 ") # no leftovers number 

#Variable 

simplehello = ("Hello")
print(  simplehello.upper()) # UpperCase
print(  simplehello.lower()) # LowerCase 
print(  simplehello.title()) # Title case  capital the frist lettre 
print(  len(simplehello)) # total carater 


# fonction

def  Presonne():
    name= input()
    age= input().upper

#if 
if len(simplehello) == 5:
    print (simplehello.upper()) 
else:
    print("byby")

# List
lotoNumber = [1, 5, 4, 9, 50, 44, 60 ]

print(lotoNumber[1])
print(lotoNumber[1:4]) # start at 1 and finish the print to 4
print(lotoNumber[:1]) # take everything befor the 1
print(lotoNumber[5:]) # take everything after the atribut 5  
print(lotoNumber[-1]) # take the last atribut 
lotoNumber.append("you can add somthing in the and of the list ")
lotoNumber.pop(0) # delete the attribut  voulu
print (lotoNumber[0])

# Tuples are a list who can be change with ()
# grades = (580, 6841, 6351, 6874, 351, 6854, 351, 654 )

# Loop
x= 0
while x < 10:
    print("so While")
    x += 1

for i in lotoNumber:
    print(i)
