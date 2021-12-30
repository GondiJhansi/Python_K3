s=input()
d=s.split()
v="aeiouAEIOU"
for i in range(len(d)):
    if d[i][0] in v:
        d[i]=d[i][::-1]
print(' '.join(d))
