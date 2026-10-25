num = 5
for row in range(num,0,-1):
    for col in range(num-row):
        print(' ',end=' ')
    for k in range(2*row-1):
        print('*',end=' ')
    print()
        
  
