n=int( input())
data=list(map(int,input().split()))
c=1
for i in range(1,n):
    if data[i]!=data[i-1]:
        print(data[i-1],end="")
        if c!=1:
            print(c,end=" ")
        c=1
    else:
        c+=1
print(data[-1],end="")
if c!=1:
    print(c)
