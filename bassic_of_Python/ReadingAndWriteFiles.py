

# Write a python script that ask for two numbers, add them together and output the response into a file called 'maths.txt'. 







# import os

# num1 = input("pls entree your frist Number")
# num2 = input("pls entree your second number")

# total = int(num2) + int(num1)

# f= open("conte2num", "w")
# f.write(f"{total} this is the total")
# f.close()


# f =open("conte2num", "r")
# print(f.read())

















# Write a python script that keeps asking for names, until they enter an empty name, then creates a file called 'people.txt' and adds names on a separate line. 



# list_name = []
# import os

# while True:
#     inputname = str(input("Entre a name pls  \n" ))
#     list_name.append(str(inputname))
    


#     if len(inputname) == 0: 
#         thenamefile = open("listname.txt", "a")
#         for x in list_name:
#             thenamefile.write(x + "\n")
#         thenamefile.close()

#         thenamefile = open("listname.txt", "r")
#         print(thenamefile.read())
#         thenamefile.close()
#         os.remove("listname.txt")
#         break

 






# Write a python script that reads a file called 'names.txt' (which has names separated by a new line), 
# then converts each name to the correct casing and outputs them to a file called 'names-formated.txt' Eg:


# lAchlan velDen -> Lachlan Velden
# Frank joe -> Frank Joe


with open("names.txt", "w") as f :

    while True:
        Fname = input("fristname pls")
        if Fname == '':pass
        Lname = input("lastname pls")
        f.write(f"{Fname} {Lname}\n")


with open("names.txt", "r") as f1 :
    fullname = f1.readline

    for w in fullname:
        print(w)

    











# Write a python script that outputs the factorial of all numbers from 1 - 10. eg:


# # output is after '->'
# 1 -> 1
# 2 = 1x2 -> 2
# 3 = 1x2x3 -> 6
# 4 = 1x2x3x4 -> 24









# Write a python script that asks for a username and password, then opens 'logins.txt' and tries to find a valid ':' separated login from this file. eg:

# file:
# user4:password3

# python output:
# username? : user4 password?: password 3 Access Granted! 