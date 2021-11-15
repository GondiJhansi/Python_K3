word=input("Enter a word ")
for ch in word:
    
    if ch in 'aeiouAEIOU':
        print(f'{word} contains vowels')
        break
    else:
        print(f'{word} contains no vowels')
