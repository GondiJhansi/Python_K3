import random
ran_num = random.randint(1,10)
guess_num = int(input("Guessed number="))

print("Random number",ran_num)

if guess_num==ran_num:
    print("Right")
else:
    print("Wrong")
    
