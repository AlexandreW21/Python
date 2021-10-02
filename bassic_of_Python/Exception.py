#  Question 1 1 pts
# Write a program called 'InputNumber' that will keep asking the user to enter a value until the value is a valid number, then print it. 


# def InputNumber():
#     while True:

#         try:
#             InputNumber1 = int(input("entre un nombre:  "))
#             print (InputNumber)
#             break

#         except ValueError:
#             print("Invalid Inpud")
    

# InputNumber()






# Write a function called 'GetIpAddress' that will keep asking the user to enter an IPv4 Address until it is valid. The function will then return the IPv4 address as a string.

# Paste only the function below.

# import ipaddress

# def GetIpAddress():
#     while True:

#         try:
#             ipv4ad = input("Enter a IPv4 address pls")
#             return(ipaddress.IPv4Address(ipv4ad))
#             break
            
#         except ipaddress.AddressValueError as va:

#             print("Entre a valide IPv4")

# GetIpAddress()





# Write a program called 'GetEmailAddress' that will keep asking the user until they enter a email address with a valid format. 
# A Valid format of an email address in this case; contains an '@', at least 1 '.' and the domain name 
# and account name is longer than 2 characters but not longer than 32 then print the Email Address as a string. 


# import re 
# #creat some exception
# class len32ex(Exception):
    
#     pass

# def GetEmailAddress():
#     while True:
#         youremail = input("Entre ton email stp")
#         checklen = len(youremail)
        
#         try:
#             #   check         -befor @  ------ after @ ----- . afer .
#             re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' , youremail) 
#             #raise the exception for check len biger of 32 and less of 6   ##@.##
#             if len(youremail) >= 32 or len(youremail) < 6 :
#                raise len32ex
#         # Simple print 
#         except len32ex :
#             print("your email is to long or to short ")

# print(GetEmailAddress())










# Write a program called 'GetPassword' that will keep asking a user to enter a password (and confirm the password) until the following criteria is met:

#     contains at least one of each:
#         a lowercase letter
#         an uppercase letter
#         a number
#         a symbol
#     is at least 7 characters long
#     does not contain the word 'password'

# The program will then output "valid password".






import re

# def GetPassword():
#     while True :
#         try:
#             secret = input("your password pls: ")
            
#             if len(secret) >= 6 and secret.isdigit() == False and secret.isalpha() == False and secret.isalnum() == False and secret.isupper() == False and secret.islower() == False and re.search("password", secret) == None: 
#                 #check all characters are not just upper or lozer case
                
# 	            return("valid password")
#         except Exception as e:
#             print("soimething wrong"+ e)
    

# print(GetPassword())










# Write a program called 'GetWordsFromUser' that takes a Min and Max as a parameter. 
# The function then takes an input from the user and ensures that the input has at least or at most the specified amount of words.Keep on asking the user until the amount of words is within range, the program then outputs all words lowercase and separated in a list. 


def GetWordsFromUser(min, max):
    
    try:
        while True:
            playerinput = input(f"Enter some world the minimun is {min} and the max is {max}, separet with a  ',' I will check: ")
            for x in playerinput.split(", ") :
                if (playerinput.count(", ") + 1 <= max) and (playerinput.count(", ") +1 >= min):
                    print(x.lower())
    except ValueError as e:
        pass


GetWordsFromUser(2, 6)




















