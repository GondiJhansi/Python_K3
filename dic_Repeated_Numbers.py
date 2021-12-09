n=int( input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for k,v in dic.items():
    print(k,end="")
    if v!=1:
        print(v,end="")
