import math
num=int(input())
n=int(math.sqrt(num))
for i in range(2,n+1):
    if(num%i==0):
        print("Not Prime")
        break
else:
    print("Prime")
