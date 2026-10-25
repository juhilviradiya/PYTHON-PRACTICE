num = 5
for row in range(num,0,-1):
    for col in range(row):
        if row == num or col == 0 or col == row - 1:
            print('*',end=' ')
        else:
            print('',end='  ')
    print()
  
