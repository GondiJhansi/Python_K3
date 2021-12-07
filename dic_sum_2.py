n=int(input())
data=list(map(int,input().split()))
dic={0:0,1:0}
for i in data:
    k=i%2
    if k not in dic:
        dic[k]=i
    else:
        dic[k]+=i
for v in dic.values():
    print(v,end=" ")
