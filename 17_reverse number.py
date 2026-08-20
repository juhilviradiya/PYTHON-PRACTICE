def reverse(num):
    num=num
    reverse = 0
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10
    return reverse
num = 14556
print(reverse(num))
