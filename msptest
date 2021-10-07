# Python Program Challenge - MSP (ENGR4)

#Written by Watts Brown

#9.28.2021

head =      "   0"
arms =      "  \|/"
torso =     "   |"
twoLegs =   "  / \ "

def body(limbs):
    print("|---┐")  
    if limbs == 4:
        print("")
        print("")
        print("")
        print("")
    if limbs == 3:
        print(head)
        print("")
        print("")
        print("")
    if limbs == 2:
        print(head)
        print(arms)
        print("")
        print("")
    if limbs == 1:
        print(head)
        print(arms)
        print(torso)
        print("")
    if limbs == 0:
        print(head)
        print(arms)
        print(torso)
        print(twoLegs)
        
def wordLength():
    length = len(word)
    print ("_ " * length)

word = input("Player 1 Enter a word")
limbs = 4
guesses = 0 
print("\n" *50 )
guess = "_ " * len(word)
body(limbs)
wordLength()
correctLetters = " "
print(guess)

while (limbs > 0 and guess != word) :
    correctGuess = False
    letterGuess = input("Player 2 Guess a letter")
    if correctLetters in word:
        correctLetters = correctLetters + letterGuess
    for spot in range(len(word)):
        if word[spot] == letterGuess:
            guess = guess[:spot] + letterGuess + guess[spot+1:]
            correctGuess = True 
            
            
    if correctGuess == False:
        limbs = limbs - 1 

    body(limbs)
    print(guess)
if(limbs == 0): 
    body(limbs)
    print("No more guesses, the word was " + word)
else: 
    print("You guessed the word! " + word)
