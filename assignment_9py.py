word = input('enter word: ')
LETTERS,DIGIT = 0,0
for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        LETTERS+=1
    elif ('0'<=i and i<='9'):
        DIGIT+=1

print(f'LETTERS: {LETTERS}\n DIGIT: {DIGIT}')
