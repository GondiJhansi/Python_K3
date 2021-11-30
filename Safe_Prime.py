from math import*
def isprime(num):
    if num==1:
        return False
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
num=int(input())
if isprime(num):
    print("Prime")
    if isprime (num//2):
        print("Semi Prime")
    else:
        print("Not a safe Prime")
else:
    print("Not a Prime")
    
