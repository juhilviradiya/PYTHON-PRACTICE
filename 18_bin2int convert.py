def bin2int(num):

    decimal = 0
    power = 0
    while num > 0:
        rem = num % 10
        decimal=decimal + rem * (2 ** power)
        num = num // 10
        power = power + 1 
    return decimal 
num = 101
print(bin2int(num))
