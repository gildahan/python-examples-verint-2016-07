from random import randint
"""
Print the sum of a the digits of a random number between 1-10000
"""


input=str(randint(1,10000))
print "Selected random number as string "  , input
sum=0
for oneChar in input:
    sum += int(oneChar)

print "The sum of the digits is : " ,sum
