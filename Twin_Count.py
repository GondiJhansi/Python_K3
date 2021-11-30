from math import*
def isprime(num):
    if num==1:
        return False
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
a,b=map(int,input().split())
c=0
while a<=b:
    if a%2 and isprime(a) and isprime(a+2):
        c+=1
        a+=2
    else:
        a+=1
print(c)
