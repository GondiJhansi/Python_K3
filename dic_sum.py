n=int(input())
data=list(map(int,input().split()))
dic={0:0,1:0}
for i in data:
    dic[i%2]+=i
for v in dic.values():
    print(v,end=" ")
