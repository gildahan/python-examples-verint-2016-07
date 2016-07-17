import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Directory")
parser.add_argument("FileSize")
args = parser.parse_args()

# (_,dir,fileSize)= sys.argv

for root,dirs,files in os.walk(args.Directory):
    for name in files:
        fullFilePath = "{}\{}".format(root,name)
        print "the file found : " ,fullFilePath
        if os.path.getsize(fullFilePath) > int(args.FileSize):
            print "Do you want to delet the file: %s\%s " % (root,name)
            print "y\\n"
            selection = raw_input()
            if  selection == "y":
                print "deleting file : " ,fullFilePath
                os.remove(fullFilePath)
print "finshed"
            
