def armstrong():

    dup = num
    n = num
    sum = 0
    power = len(str(num))

    while n > 0:

        rem = n % 10
        sum = sum + rem ** power
        n = n // 10

    if dup == sum:
        return "armstrong"
    else:
        return "not armstrong"
num = 153
print(armstrong())
