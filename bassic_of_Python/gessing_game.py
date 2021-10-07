"""
Start Game 
    - creat random number 1 to 25
    - Creat log guessing number array
    - Limite the guess number to 7 loop 7 time in total     (loop)
        
        - ask for user input                        
        - Check userinput with the random numbre            (if else statment)
            if win
                -print winning message + numbre chance left + log number  
                -end the game because win  
            elif greter
                print greater message 
            elif less
                print less message
            print guess left
    -loop finish meaning the player loss
    -display loss message + logNumber + guessing try      

"""
import random 




print("Hey there! Lets play a little guessing game. \n Guess the number between 0 and 25")

randomNum = random.randint(1, 25) # creat random Number and stock in variable
maxTry = 7  # Chance variable 
guessLog = [] # log array


for i in range(0, maxTry):                                     # linite input 
    inputUser = int(input("Enter Guess: "))                    # input user 
    guessLog.append(inputUser)                                 # adding number in guesselog 


    if inputUser == randomNum:                                 # win 
        print(f"The numbre was indeed {randomNum}")
        print(f"You guessed in {i + 1} guesses")
        print(f"Your guess log: {guessLog}")
        break                                                  #  break the game resul find 



    elif inputUser < randomNum:                                # greter
        print("Nope, its is greter  than that")                
        continue                                             
    elif inputUser > randomNum:                                # less
        print("Nope, its less than that")
        continue

    print(f"You have {(maxTry - i - 1)} guesses left!")        # chancenumber - try -1   the -1  is because the loop start by 0 

print("AHHAHA YOU LOSE!")                                      #Lose message 
# print(f"The number was {randomNum } you fool.")
# print(f"Your guesslog: {guessLog}")
    
    

