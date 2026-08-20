def int2bin(num):
    binary=""
    while num > 0:
        rem = num % 2
        binary=str(rem) + binary
        num = num // 2
    return "ob" + binary
num = 6
print(int2bin(num))
