import sys
import os

if len(sys.argv) != 3 :
    print "Not enogh paraeters "
    sys.exit(1)

(_,firstNum,secNum) = sys.argv

print "the sum is" , int(firstNum) + int (secNum) 