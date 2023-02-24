a = input('enter binary number: ').split(',')
lst = []

for i in a :
    if(len(i)>4 or len(i)<4):
        print('please enter only 4 digit binary number\n')
        break
    elif int(i,2)%5==0:
        lst.append(i)    

print(','.join(lst))


