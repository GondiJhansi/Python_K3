n=int(input())
s=0
sq=n*n
while sq!=0:
    r=sq%10
    s=s+r
    sq=sq//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")
