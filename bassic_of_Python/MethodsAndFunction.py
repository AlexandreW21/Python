# 0. Write a Python function to add two numbers and return the value

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# Write the function between the START and END tags
# START

# def AddTwoNumbers(num1, num2):
#     total = num1+num2 
#     return(total)


# # # END
# # # -------------------------------------
# # # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
# print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))




















# . Write a Python function to add a string in-between two strings and return it.

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# # Write the function between the START and END tags
# # START



# def AddInString(str1, name, str2):
#      return(f"{str1}{name}{str2}")






# # # END
# # # -------------------------------------
# # # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(AddInString("Hello, ", "bob", ". How are you today?") == "Hello, bob. How are you today?"))
# print("Test 2 Passed: " + str(AddInString("Woah there ", "frank", ", watch your step!") == "Woah there frank, watch your step!"))
# print("Test 3 Passed: " + str(AddInString("Whats the , ", "meaning", " of all of this?") != "What is the meaning of all of this"))
# print("Test 4 Passed: " + str(AddInString("Happy ", "Lappy", " Tappy") == "Happy Lappy Tappy"))























# Write a Python function that returns the sum of all numbers of Fibonacci to the provided count. 

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# # Write the function between the START and END tags
# # START

# def FibonacciAdder(num):

#     numA = 0 
#     numb = 1
#     total = 0

#     if num == 1  :
#         return(0)
#     elif num == 2 :
#         return(1)
#     else:
#         for i in range(num):
#             total = numA + numb
#             numA = numb
#             numb = total
#         return(total - 1 )





# # END
# # -------------------------------------
# # DO NOT TOUCH ANY CODE BELOW THIS LINE

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ..


# print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
# print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
# print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))



























# 1. Write a Python function to multiply all the numbers in a list called 'MultiplyElementsInList'.

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# # Write the function between the START and END tags
# # START

# def MultiplyElementsInList(thelist):
#     total = 1
#     for i in thelist:
#         total = total * i
#     return total



# # # END
# # # -------------------------------------
# # # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(MultiplyElementsInList([1, 2, 3]) == 6))
# print("Test 2 Passed: " + str(MultiplyElementsInList([0, 2, 3]) == 0))
# print("Test 3 Passed: " + str(MultiplyElementsInList([2, 2, 2]) == 8))
# print("Test 4 Passed: " + str(MultiplyElementsInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 30414093201713378043612608166064768844377641568960512000000000000))



























# 2. Write a Python function that checks whether a passed string is palindrome or not called 'IsPalindrome' that returns either True or False.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# # # Write the function between the START and END tags
# # # START





# def IsPalindrome(string):
#     stringup = string.upper().replace(' ', '')
#     if(stringup == stringup[:: -1]):
#         return True
#     else:
#         return False
    

# # # END
# # # -------------------------------------
# # # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
# print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
# print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
# print("Test 4 Passed: " + str(IsPalindrome("frank") == False))






































# 3. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically called 'SortWordsAlphabetically'.

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# # Write the function between the START and END tags
# # START


# def SortWordsAlphabetically(mot):

#     mots = [mot.lower() for mot in mot.split("-")]
#     mots.sort()
#     mot = "-".join(mots)
#     return mot

# # # END
# # # -------------------------------------
# # # DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
# print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
# print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))
































# Write a function called 'PrintBoxByWidth' that prints out a box that looks like below, at the specified width. DO NOT add or edit any print statements in the code provided; you may only move them around your code.

# PrintBoxByWidth(60) => 
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# x                                                          x
# xoooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
# x                                                          x
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def PrintBoxByWidth(taile):


    for i in range(0,5):
        print("x", end='')
        if i == 1 or i == 3:
            for taile in range(0,58):
                print(" ", end='')
            print("x", end='')
        if i == 2:
            for taile in range(0,58):
                print("o", end='')
            print("x", end='')
        if i == 0 or i == 4:
            for taile in range(0,59):
                print("x", end='')
        print("")

PrintBoxByWidth(60)