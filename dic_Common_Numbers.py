n1=int(input())
data1=list(map(int,input().split()))
n2=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=0
for k,v in dic.items():
    if v==0:
        print(k,end=" ")

