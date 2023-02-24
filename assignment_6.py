a = input('enter words: ').split(' ')
for i in a :
    if a.count(i)>1:
        a.remove(i)

b = sorted(a)
print(' '.join(b))