a = input('enter numbers: ').split(',')
lst = []
for i in a :
    if(int(i)%2!=0):
        b = int(i)*int(i)
        c = str(b)
        lst.append(c)
print(','.join(lst))