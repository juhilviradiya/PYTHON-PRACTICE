# Count Frequency of a Digit
# Given a positive integer N and a digit D, count how many times digit D appears in N.

num = int(input("Enter the number is : "))
D = int(input("Enter the number is : "))
count = 0
while num > 0:
    rem = num % 10
    if rem == D:
        count = count + 1
    num = num // 10
print(count)
