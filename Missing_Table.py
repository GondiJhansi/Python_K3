n,r=map(int,input().split())
for i in range(1,r+1):
    if i%n==0:
       continue
    print(n,"X",i,"=",n*i)
