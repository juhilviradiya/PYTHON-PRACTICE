'''
Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
'''

def number(num):
    if num[0] == num[-1]:
        return True
    else:
        return False
        
        
num = [10,20,30,40,50,100]
print('Result is :',number(num))



