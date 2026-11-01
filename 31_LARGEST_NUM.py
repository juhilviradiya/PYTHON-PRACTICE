# Find the Largest Digit using loop

num = int(input("Enter the number is : "))
largest = 0 # 456
while num > 0:
    rem = num % 10
    if rem  > largest :
        largest = rem
    num = num // 10
print("largest number is : ",largest)
