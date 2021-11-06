n,r1,r2=map(int,input().split())
if r1<r2:
    for i in range (r1,r2+1):
        print(n,"X",i,"=",n*i)
else:
    for i in range (r2,r1+1):
        print(n,"X",i,"=",n*i)
