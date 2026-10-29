'''
Practice Problem: Write a program to check if a given number is a palindrome reads the same forwards and backwards).
'''

num = int(input('Enter the number is : '))
dup = num
ans = 0
while num > 0:
    rem = num % 10
    ans = ans * 10 + rem
    num = num // 10
if dup == ans:
    print("The number is palimdrome")
else:
    print("The number is not palimdrome")
