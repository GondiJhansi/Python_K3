n=int(input())
e_c=0
o_c=0
c=0
while n!=0:
    c+=1
    r=n%10
    n=n//10
    if r%2==0:
        e_c+=1
    else:
        o_c+=1
if e_c==c:
    print("Even ")
elif o_c==c:
    print("Odd ")
else:
    print("Mixed")
