import sys 

(_,fin , fout) = sys.argv

with open(fin,"r") as f1:
    with open(fout,"a") as f2:
        for line in f1:
            f2.write(line)

