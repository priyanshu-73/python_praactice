word = input('enter sentence: ')
upper,lower = 0,0
for i in word:
    if('a'<=i and i<='z'):
        lower+=1
    elif('A'<=i and i<='Z'):
        upper+=1

print(f'UPPER: {upper}\n LOWER: {lower}')