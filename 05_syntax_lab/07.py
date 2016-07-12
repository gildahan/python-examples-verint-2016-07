from random import randint

"""
Guess the number
"""

i=1
machineNum = randint(1,100)

print "The Machinenumber is " ,machineNum

userNum =0
while userNum != machineNum: 
    userNum = int(raw_input())
    if userNum > machineNum: 
        print "Too Big"
    else:
        print "Too small"

print "CORRECT -  Thanks For playing"