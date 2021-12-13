
n=int(input())
rev=0
temp=n
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp==rev:
    print("True")
else:
    print("False")
    
    
    
