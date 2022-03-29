"""
Collatz sequence
3 10 5 16 8 4 2 1
"
"""
a=int(input())
while a!=1:
    print(a,end=" ")
    if a%2!=0:
        a=a*3+1
    else:
        a=a//2
print(a)
    

