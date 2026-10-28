num = 1634
dup = num
ans = len(str(num))
total = 0
while num > 0:
    rem = num % 10
    total = total + rem ** ans
    num = num // 10
if dup == total:
    print("Narcissistic Number")
else:
    print("Not Narcissistic Number")
    
