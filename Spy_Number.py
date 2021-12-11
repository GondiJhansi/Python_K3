n=int(input())
s=0
pro=1
while n !=0:
    r=n%10
    s=s+r
    pro=pro*r
    n=n//10
if s==pro:
    print("Spy Number")
else:
    print("Not Spy Number")
