# Python Program Challenge - MSP (ENGR4)

#Written by Watts Brown

#9.28.2021

head =      "   0"      #variables to call for the msp drawing function
arms =      "  \|/"
oneArm =    "  \|"
torso =     "   |"
twoLegs =   "  / \ "
oneLeg =    "  /"

def body(limbs):  #function to draw the msp when the player gets a letter wrong
    print("|---┐")  
    if limbs == 7:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    if limbs == 6:
        print(head)
        print("")
        print("")
        print("")
        print("")
        
    if limbs == 5:
        print(head)
        print(oneArm)
        print("")
        print("")
        print("")
        
    if limbs == 4:
        print(head)
        print(arms)
        print("")
        print("")
        print("")
        
    if limbs == 3:
        print(head)
        print(arms)
        print(torso)
        print("")
        print("")
        
    if limbs == 2:
        print(head)
        print(arms)
        print(torso)
        print(oneLeg)
        print("")
        
    if limbs == 1:
        print(head)
        print(arms)
        print(torso)
        print(twoLegs)
        print("")
        
    if limbs == 0:
        print(head)
        print(arms)
        print(torso)
        print(twoLegs)
        print("")

word = input("Player 1 Enter a word") #player one's input.
limbs = 7  #number of lives player 2 has
guesses = 0 
print("\n" *50 )
guess = "_" * len(word) #sets "_" for missing letter spots
body(limbs) 
correctLetters = " "
print(guess)

while (limbs > 0 and guess != word) : #loop for player two's guess and seeing if it is right or wrong
    correctGuess = False
    letterGuess = input("Player 2 Guess a letter")
    if correctLetters in word:
        correctLetters = correctLetters + letterGuess
    for spot in range(len(word)):
        if word[spot] == letterGuess:
            guess = guess[:spot] + word[spot] + guess[spot+1:]
            correctGuess = True 
            
            
    if correctGuess == False:
        limbs = limbs - 1 

    body(limbs)
    print(guess)
if(limbs == 0): #Tells you if you win or not when the game is over
    body(limbs)
    print("No more guesses, the word was " + word)
else: 
    print("You guessed the word! " + word)
