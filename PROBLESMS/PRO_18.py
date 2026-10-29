'''
Practice Problem: Write a program to extract each digit from an integer in the reverse order.
'''
num = int(input("Enter The number is : "))
ans = 0
while num > 0:
    rem = num % 10
    ans = ans * 10 + rem
    num = num // 10
print(f'The reverse number is : {ans}')
