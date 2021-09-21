# Python Program 02 - Quadratic Solver (ENGR4)

#Written by Watts Brown

#9.121.2021
from math import sqrt

def discriminate():
    dis = b * b - 4 * a * c 
    if dis > 0: 
        print(" real and different roots ") 
        ans1 = (-b-sqrt(dis))/(2 * a)
        ans2 = (-b + sqrt(dis))/(2 * a)
        print("root 1: ", ans2)
        print("root 2: ", ans1)
    elif dis == 0: 
        print(" real and same roots" ) 
        print ("root 1: ", -b / (2 * a))
        
    elif dis < 0:
        print(" no real roots")
a = int(input("Enter coeeficient a: "))
b = int(input("Enter coeeficient b: "))
c = int(input("Enter coeeficient c: "))
discriminate()



x = input("Press x to quit Press enter to run again")
while x == (""):
    a = int(input("Enter coeeficient a: "))
    b = int(input("Enter coeeficient b: "))
    c = int(input("Enter coeeficient c: "))
    discriminate()

    
    x = input("Press x to quit Press enter to run again")
print("Goodbye!")
 
