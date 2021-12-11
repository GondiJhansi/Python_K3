n=int(input())
summ=0
pro=1
while n!=0:
    r=n%10
    summ=summ+r
    pro=pro*r
    n=n//10
    result=pro-summ
print(result)
    
