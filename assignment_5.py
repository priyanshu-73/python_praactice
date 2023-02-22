x,y = map(int,input('enter numbers: ').split(','))
lst = [[i*j for j in range(y)]for i in range(x)]
print(lst)