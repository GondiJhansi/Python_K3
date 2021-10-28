English = int(input())
Telugu = int(input())
Hindi = int(input())
Maths = int(input())
Science = int(input())
Social = int(input())

total = English+Telugu+Hindi+Maths+Science+Social
Total_Marks=100
per = total//6
print("total marks",total)
print("Percentage : ",per)


if English>=35:
    print("English  ","   ",English,     Total_Marks,      "P"  )
else:
    print("English  ","   ",English,     Total_Marks,      "F"  )
if Telugu>=35:
    print("Telugu   ","   ",Telugu,      Total_Marks,      "P"  )
else:
    print("Telugu   ", "   ",Telugu,      Total_Marks,      "F"  ) 
if Hindi>=35:
    print("Hindi    ","   ",Hindi,       Total_Marks,      "P"  )
else:
    print("Hindi    ","   ",Hindi,       Total_Marks,      "F"  )
if Maths>=35:
    print("Maths    ","   ",Maths,       Total_Marks,      "P"  )
else:
    print("Maths    ","   ",Maths,       Total_Marks,      "F"  )
if Science>=35:
    print("Science  ","   ",Science,     Total_Marks,      "P"  )
else:
    print("Science  ","   ",Science,     Total_Marks,      "F"  )
if Social>=35:
    print("Social   ","   ",Social,      Total_Marks,      "P"  )
else:
    print("Social   ","   ",Social,      Total_Marks,      "F"  )
print("score:" ,total,",","Per:",per)
