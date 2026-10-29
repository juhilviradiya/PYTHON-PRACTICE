'''
Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.
'''
num = 5
for row in range(1,num + 1):
    for col in range(1,row + 1):
        print(row,end= ' ')
    print()
