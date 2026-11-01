# Product of Digits
num = int(input("Enter the number is : "))
product = 1
while num > 0:
    rem = num % 10
    product = product * rem
    num = num // 10
print("product is :",product)
