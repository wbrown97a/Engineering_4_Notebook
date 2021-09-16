# Python Program 01 - Calculator (ENGR4)
#Written by Watts Brown
#9.16.2021

#doMath function creation
def doMath(a,b,flag):
    if flag == 1:
      #return returns it to the function to output it in the print
      #str turns the number into a string so you can print it out
        return str(a + b)
    if flag == 2:
       return str(a - b)
    if flag == 3:
        return str(a * b)
    if flag == 4:
      #round function rounds the long decimals to whatever number you put after the comma to have cleaner decimals
      return  str (round(a / b, 2))
    if flag == 5:
        return str(a % b)
    
    
a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
#numbers in doMath function are flags that tell it what equation to do
print("Sum: " + doMath(a,b,1))
print("Difference: " + doMath(a,b,2))
print("Product: " + doMath(a,b,3))
print("Quotient: " + doMath(a,b,4))
print("Modulo: " +  doMath(a,b,5))
