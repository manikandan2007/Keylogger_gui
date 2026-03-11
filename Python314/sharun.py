fname=input("enter file name:")
with open(fname,'r')as f:
    for line in f:
        print(line.upper())
