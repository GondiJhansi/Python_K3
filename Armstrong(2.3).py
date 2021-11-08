num = int(input("Enter a number ="))
sum=0
temp = num
while (temp>0):
    rem = temp % 10
    sum = sum+(rem*rem*rem)
    temp = temp // 10

if num==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")


