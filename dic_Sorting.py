n=int(input())
data=list(map(int,input().split()))
dic={}
data.sort()
data.reverse()
for i in data:
    dic[i]=1
for k,v in dic.items():
    print(k,end=" ")
