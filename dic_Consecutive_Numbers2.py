n=int(input())
data=list(map(int,input().split()))
dic={1:0}
c=0
for i in data:
    if i==1:
        c+=1
    else:
        c=0
    if dic[1]<c:
        dic[1]=c
print(dic[1])
