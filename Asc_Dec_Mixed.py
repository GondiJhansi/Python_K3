n=int(input())
d1=n%10
n=n//10
d2=n%10
n=n//10
if d1>d2:
    asc=1
    dec=0
else:
    dec=1
    asc=0
while n:
    d=n%10
    n=n//10
    if asc==1 and d>d2:
        print("Mixed")
        break
    if dec==1 and d<d2:
        print("Mixed")
        break
    d2=d
else:
    if asc==1:
        print("asc")
    else:
        print("dec")
