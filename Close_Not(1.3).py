num1 = float(input("Enter 1st number="))
num2 = float(input("Enter 2nd number="))
diff = num1 - num2
if diff<0.001 :
    print("Close")
else:
    print("Not close")
