# Python Program 01 - Calculator (ENGR4)

#Written by Watts Brown

#9.23.2021

str1 = input("Enter a sentence: ") #gets sentence from user
str2 = str1.split() #splits sentence into seperate words


for word in str2: #gets each word in str1
    
    
    for letter in word: #seperates and prints each letter in each word
        print(letter)
    print("-") #prints dash inbetween each word
