from math import *
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
    np=num+2
    while True:
        if isprime(np):
            break
        else:
            np+=2
    pp=num-2
    while True:
        if isprime(pp):
            break
        else:
            pp-=2
    if np*pp<=num*num:
            print("good prime")
    else:
            print("baad prime")
else:
    print("Not Prime")
