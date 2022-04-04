n=input()
s=str(n)
l=[]
for i in s:
    l.append(i)
c=[]
for i in l:
    if i not in c:
        c.append(i)
if len(l)==len(c):
    print("Unique Number")
else:
    print("Not Unique Number")
    
