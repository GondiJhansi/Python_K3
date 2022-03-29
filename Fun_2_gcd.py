def find_gcd(a,b):
    if a>b:
        a,b=b,a
    while a:
        b=b%a
        a,b=b,a
    return b
a,b=map(int,input().split())
gcd=find_gcd(a,b)
print(gcd)

        
    
