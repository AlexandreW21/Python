################################################## Question 1 #####################################################
# Given the following python code:
# values = [66, 43, 1, 6, 2, 99, 4]
# Output each number on a separate line if it is less than the number 10.



Values = [66, 43, 1, 6, 2, 99, 4]

for x in Values:
    if x < 10:
        print(x)



################################################## Question 2 #####################################################
# Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
# The date will be printed like below:
# Date: 23
# Month : 08
# Year: 2019


dateinput = input("Date pleas").split('/')

print ("Date: ", dateinput[0])
print ("mounth: ", dateinput[1] )
print ("Years: ", dateinput[2])



################################################## Question 3 #####################################################

# Given the following python code
# values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
#     Sum all of the numbers and output the result
#     Average all of the numbers and output the result
#     Output the maximum number in the list




values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]

print("Total: ", sum(values)  , "\nAverage Number: ", sum(values) / len(values) , "\nMax Number: ", max(values))




################################################## Question 4 #####################################################
# Write a program that enters a string containing a person's full name and then output their initials. Example:
# Full Name: Lachlan van der Velden
# Initials: LVDV

# Full Name: Dave Verg Douglas
# Initials: DVD




inputUser = input("What is your full name? ").split()

print("Full Name: ", inputUser)

firsts = [w[0].capitalize() for w in inputUser]
print("Initials: ", firsts) 





################################################## Question 5 #####################################################
# Write a program that can accept many numbers from the user, until they enter an x. Example:
# Enter a number: 5
# Enter a number: 9
# Enter a number: 3
# Enter a number: 12
# Enter a number: x
# You entered: [5, 9, 3, 12]


DataBaseNum = []

while True:
    inputUser = input("Enter a number:" )

    if inputUser == "x":
        print(DataBaseNum)
        break
    else:
        DataBaseNum.append(inputUser)




################################################## Question 6 #####################################################
# Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:
# Enter a large number: 29834892
# Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45

Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    print(Reminder)
    Sum = Sum + Reminder
    Number = Number //10
print(Sum)

################################################## Question 7 #####################################################
# Write a program to ask the user for numbers, and then print any repeating numbers in a list. Example:
# Enter a number: 5
# Enter a number: 2
# Enter a number: 6
# Enter a number: 98
# Enter a number: 7
# Enter a number: 6
# Enter a number: 5
# Enter a number: x
# Repeating numbers: [5, 6]


DataBaseNum = []
duplicate = set()

while True:
    inputUser = input("Enter a number:" ) #gipe asking for number

    if inputUser == "x": # stop with the lettre x
        print(DataBaseNum)
        print(duplicate) # print the reponce
        break            # break the loop  
    else:
        DataBaseNum.append(inputUser) # add numbre in database
        for x in DataBaseNum:
            if DataBaseNum.count(x) > 1:
                duplicate.add(x)
                continue
            else:
                continue
        
                




