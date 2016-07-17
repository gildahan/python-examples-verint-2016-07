import sys 

(_,fin1,fin2 , fout) = sys.argv
array1 = []
array2 = []
with open(fin1,"r") as f1:
    for line in f1:
        array1.append(line)
with open(fin2,"r") as f2:
    for line in f2:
        array2.append(line)
with open(fout,"a") as f3:
    if len(array1)>len(array2):
        for count in range(len(array1)):
            f3.write(array1[count])
            if len(array2)>count:
                f3.write(array2[count])
    else:
        for count in range(len(array2)):
            if len(array1)>count:
                f3.write(array1[count])
            f3.write(array2[count])
            