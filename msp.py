# Python Program Challenge - MSP (ENGR4)

#Written by Watts Brown

#9.28.2021

head =    "   0"
twoArms = "  \|/"
torso =   "   |"
twoLegs = "  / \ "

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
        print(twoArms)
        print("")
        print("")
    if limbs == 1:
        print(head)
        print(twoArms)
        print(torso)
        print("")
    if limbs == 0:
        print(head)
        print(twoArms)
        print(torso)
        print(twoLegs)
        
def wordLength():
    length = len(word)
    print ("_ " * length)

word = input("Player 1 Enter a word")
limbs = 4
guesses = 0 
print("\n" *50 )
wordLength()
guess = input("Player 2 Guess a letter")
letter = list(word)
body(limbs)

while (limbs > 0 and guess != word) :
    failed = 0 
