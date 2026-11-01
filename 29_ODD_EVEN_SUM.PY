# Your task is to calculate:
# 1)Sum of even digits.
# 2)Sum of odd digits.

num = int(input("Enter the number is : "))
even_total = 0
odd_total = 0
while num > 0:
    rem = num % 10
    if rem % 2 == 0:
        even_total = even_total + rem
    else:
        odd_total  = odd_total + rem
    num = num // 10
print(even_total)
print(odd_total) 
