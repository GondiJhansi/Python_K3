n,d=map(int,input().split())
c=0
while n:
    r=n%10
    if r>=d:
        c+=1
    n=n//10
print(c)
