"""
Print thr bigest number between 10 inputs
"""
newX=0
i=0
while  i < 10:
     print "insert a number " ,i+1
     x=int(raw_input())
     i+=1
     if    x>newX:
         newX =x    

print "The biggest number is: " , newX