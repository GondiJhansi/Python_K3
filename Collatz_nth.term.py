n,t = map(int,input().split())
c=1
while True:
    if c==t:
        print(n)
        break
    if n==1:
        print(-1)
        break
    if n%2:
        n=n*3+1
    else:
        n=n//2
    c+=1
    
