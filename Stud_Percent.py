"""s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
s6 = int(input())"""
s1,s2,s3,s4,s5,s6=map(int,input().split())


total = s1+s2+s3+s4+s5+s6
per = total//6
print(total,per)
c=0
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
    print("Pass")
    if per>=80:
        print("First")
    elif per>=65:
        print(" Second")
    elif per>=50:
        print("Third")
else:
    print("Fail")
    if s1<35:
        c+=1
        print("Failed in s1")
    if s2<35:
        c+=1
        print("Failed in s2")
    if s3<35:
        c+=1
        print("Failed in s3")
    if s4<35:
        c+=1
        print("Failed in s4")
    if s5<35:
        c+=1
        print("Failed in s5")
    if s6<35:
        c+=1
        print("Failed in s6")
    print("No of failed subjects",c)
