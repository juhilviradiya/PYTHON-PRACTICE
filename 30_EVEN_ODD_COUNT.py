#  Count Even and Odd Digits
# 1)Total even digits.
# 2)Total odd digits.

num = int(input("Enter the number is : "))
even_count = 0
odd_count = 0
while num > 0:
    rem = num % 10
    if rem % 2 == 0:
        even_count=even_count + 1
    else:
        odd_count = odd_count + 1
    num = num // 10
print("Even Count :",even_count)
print("Odd Count :",odd_count)
