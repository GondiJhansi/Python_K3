n=int(input())
Factor_Count=0
for i in range(1,n+1):
    if n%i==0:
        Factor_Count+=1
print(Factor_Count)
    
