'''
Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.
'''
num_list = [10, 20, 33, 46, 55]
print('divisible 5 ')
for ans in num_list:
    if ans % 5 == 0:
        print(ans)
