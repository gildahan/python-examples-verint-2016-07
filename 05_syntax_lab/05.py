from random import randint
from array import array

"""
Finding a number deviding 15 , 13 ,7
"""

num = randint(1,1000000)
while (num % 7 != 0) or (num % 13 != 0) or (num % 15 != 0): 
    print "The current selected numer is : " , num
    num = randint(1,1000000)
    
print "The winner num is :", num

