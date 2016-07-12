from random import randint
from array import array

"""
The small number dividing two numbers
"""

i=1
num1 = randint(1,10)
num2 = randint(1,10)  
print "The numbers are :{},{}".format(num1 ,num2)

while True: 

    if num1>num2: 
        if (num1*i)%num2 == 0:
            finalNum = (num1*i)
            break
    else:
        if (num2*i)%num1 ==0 :
            finalNum = (num2*i)
            break
    i+=1   
print "The small number is: " , finalNum 