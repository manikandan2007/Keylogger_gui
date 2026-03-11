def gcd(a,b):
    if(b==0):
        return 0
    else:
        return gcd(b,a%b)
a=int(input("enter first number:"))
b=int(input("enter second nnumber:"))
GCD=gcd(a,b)
print("GCD is:",GCD)
