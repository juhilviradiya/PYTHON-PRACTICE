num = 5
for row in range(1,num+1):
    for col in range(1,row+1):
        if col==1 or row == num or col == row:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

