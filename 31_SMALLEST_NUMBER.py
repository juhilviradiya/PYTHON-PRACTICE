#Find the Smallest Digit using loop


num = int(input("Enter the number is : "))
smallest = 0
while num > 0:
    rem = num % 10
    if rem < smallest:
        smallest = rem
    num = num // 10
print("smallest number is :",smallest)

