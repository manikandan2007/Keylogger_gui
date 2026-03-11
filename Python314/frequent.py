from frequentword import counter
def wordCount(fname):
    with open(fname)as f:
        return counter(f.read().split())
        print("number of words in the file:/n",wordcount("test.txt"))

 
