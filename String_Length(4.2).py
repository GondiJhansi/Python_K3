s1=input("Enter 1st string")
s2=input("Enter 2nd string")
l1=len(s1)
l2=len(s2)
if l1!=l2:
    print("Both the strings are not equal")
else:
    s=" "
    for i in range(l1):
        s+=s2[i]+s1[i]
        print(s)
