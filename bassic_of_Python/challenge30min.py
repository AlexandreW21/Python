# 1.	Using a python script:
# a.	Read the specified details from the user (First Name, Last Name, Age).
# i.	This will mean that your application must accept ANY name and age combination not just the ones from the examples.
# b.	Process their age depending on your Student ID
# i.	If the 3rd last digit of your student id is a 0, do not offset the age by anything.
# ii.	You MUST hard code this digit in your script, do not ask for it.
# iii.	If you do not know your student ID, it is the numbers used when signing into anything Swinburne related.
# c.	Generate and output a pipe (‘|’) separated email and password combo.
# i.	This output will be like the example provided, but with the provided name and age used instead.
# d.	Keep asking until the user has entered an empty first name

id = 103083520              #Student ID

offset = int(str(id)[-3])   # the offset of the age change the number by the 3 last digit of your sudent ID

database = []


print("You can exit the programe by leaving the Frist name allocation empty")

while True:     #loop the programe until  the breack commande are ritch 
                    
    fName = input(str("First Name: "))  # this is the fristname of the traget 
    if not fName:
        for x in database:
            print(x)
        break 
    lName = input("Last Name: ")        # this is the lastname of the traget
    age = int(input("Age: "))           # Age you the traget 
    year = 2021                         # the desired year  
    userYear = (year - age + offset)    # calculation of the year of birth  + the offset 
    
    

    database.append(f"{fName.lower()[:1]}{lName.lower()}@huawow.io | {fName.lower()}{lName.capitalize()[:1]}_{userYear}")

