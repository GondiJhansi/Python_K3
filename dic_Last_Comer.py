n=int(input())
data=list(map(int,input().split()))
dic={}
data.sort()
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v==1:
        d=k
print(d,end=" ")

        
        

    
