~
#Question 1#######################################################################################################################################################################################################################################################################
#Write a program that asks the user for their name, checks if their name is either "frank" or "george" and if it is, greet them by their name.

name = input("Hi there what is you name pleas? \n")

if name == "frank" or  "george":
    print(f"Hello {name}")
else:
    print(f"Hello {name}")

#Question #######################################################################################################################################################################################################################################################################
#Write a program that asks the user for their year of birth, checks if they are of legal drinking age, and tells the user to come into the bar. Example:



Year = int(input("What is tou Year Of Birth \n"))
totalAge = 2121 - Year 

if totalAge > 18 :
    print("\n Come in and have a drink! \n ")
else:
    print("\n Go away. Child. \n")

#Question 3#######################################################################################################################################################################################################################################################################
# # Write a program that could be used for an (unsecure) login, with a username1 and password. For example:


# database
userName1 = "bob"
Passworld = "password1234"
userName2 = "frank"
Passworld2 = "goodpassworld"

# input user 1
userName1Input = input("Enter username Pleas \n ")
userName1password = input("Enter password please \n ")

# logique user 1
if userName1 == userName1Input and Passworld == userName1password:
    print("Access Granted!")
else:
    print("Access Denied!")


#  input user 2
userName2Input = input("Enter username Pleas \n ")
userName2password = input("Enter password please \n ")    

#  logique user 2
if userName2 == userName2password and Passworld2 == userName2password:
    print("Access Granted!")
else:
    print("Access Denied!")

#Question 4#######################################################################################################################################################################################################################################################################
# Copy and Modify Question 3, to support the following username password combinations:

#     bob : password1234
#     fred : happyPass122
#     lock: passwithlock44

# Please ensure that the password only works with the corresponding username.

credenciel = [
    {
        'name': "bob",
        'passworld':  "passwoprld1234"
    },
    {
        'name': "fred",
        'passworld':  "happyPass122"
    },
    {
        'name': "lock",
        'passworld': "passwithlock44"
    }

]

search = input("What is your name pleas?")
passworlInput = input("What is your passworld?")
for x in range(len(credenciel)):
    if search.lower() in credenciel[x]['name'].lower():
        if credenciel[x]['passworld'].lower() == passworlInput:

            print('name: ',credenciel[x]['name'])
            print('passworld: ', credenciel[x]['passworld'])
            break
        else:
            print('Invalid Entry!')
    else:
        print("We can not find your name in the database")    
        break    
 


#Question 5 #######################################################################################################################################################################################################################################################################

# Write a program that can grade a student based upon a percentage grade. Example:

# What was your grade: 99
# You will receive a "High Distinction"

# Please use the following grade table within your application:
# High Distinction 	100 - 90
# Distinction 	89- 80
# Credit 	79 - 70
# Pass 	69 - 50



GradeInput = int(input("What was your grade:"))
HighDistinction = range(90,101)
Distinction = range(80,90)
Credit = range(70,80)
Pass = range(50,70)

if GradeInput in HighDistinction: 
    print("You will receive a 'High Distinction'")
elif GradeInput in Distinction: 
    print("You will receive a 'Distinction'")
elif GradeInput in Credit: 
    print("You will receive a 'Credit'")
elif GradeInput in Pass: 
    print("You will receive a 'Pass'")
else:
    print("Invalide input") 

# #######   try some 





# credenciel = [
#     {
#         'name': "bob",
#         'passworld':  "passwoprld1234"
#     },
#     {
#         'name': "fred",
#         'passworld':  "happyPass122"
#     },
#     {
#         'name': "lock",
#         'passworld': "passwithlock44"
#     }

# ]


# search = input("What is your name?")
# passworlInput = input("What is your passworld?")
# for x in range(len(credenciel)):
#     if search.lower() in credenciel[x]['name'].lower():
#         if credenciel[x]['passworld'].lower() == passworlInput:

#             print('name: ',credenciel[x]['name'])
#             print('passworld: ', credenciel[x]['passworld'])
#             break
# else:
#     print('Invalid Entry!')
 


# credenciel0 = {
#     "name": "bob",
#     "passworld": "passworld1234"
# }
# credenciel1 = {
#     "name": "fred",
#     "passworld": "passworld1234"
# }
# credenciel2 = {
#     "name": "lock",
#     "passworld": "passworld1234"
# }






# credencielList = [credenciel0, credenciel1, credenciel2]


# userName1Input = input("whatis your name? ")

# for x in credencielList:
#     for x1 in x:
#         if slice(credencielList[x1]) == slice(userName1Input): 
#             print("okokokok")
#         else:
#             print("nobody by this name ")




    # if 
    #     if credenciel["name"] == nameInput:
    #         print("ok")
    #     else:
    #         print("no name in the database ")


