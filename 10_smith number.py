num = int(input("enter the number : "))
dup = num

# sum of digits of original number
sum1 = 0
while num > 0:
    rem = num % 10
    sum1 = sum1 + rem
    num = num // 10

# sum of digits of prime factors
num = dup
sum2 = 0
i = 2

while i <= num:
    while num % i == 0:
        temp = i

        while temp > 0:
            rem = temp % 10
            sum2 = sum2 + rem
            temp = temp // 10

        num = num // i

    i = i + 1

if sum1 == sum2:
    print("smith number")
else:
    print("not smith number")
