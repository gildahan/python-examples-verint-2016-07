from random import randint
"""
Print the sum of a 7 random number between 1-100
"""
newX=0
i=0
while  i < 7:
     x=randint(1,100)
     print i+1 ,"- select random number "  , x
     
     newX+=x
     i+=1
    
print "The sum is: ", newX

if newX % 7 == 0 :
    print "Deviding By 7 So ....Boom " 