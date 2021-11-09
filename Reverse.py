n=int(input())
for i in range(1,n*2):
    if i<=n:
        print(i,end=" ")
    else:
        n=n-1
        print(n,end=" ")
