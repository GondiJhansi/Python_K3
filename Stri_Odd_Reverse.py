s=input()
d=s.split()
for i in range(len(d)):
    if i%2==0:
        print(d[i][::-1],end=" ")
    else:
        print(d[i],end=" ")
    

        
