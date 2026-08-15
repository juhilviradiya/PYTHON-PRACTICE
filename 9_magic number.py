num=int(input("enter the number : "))
while num > 9:
    sum=0
    while num>0:
        rem=num % 10
        sum=sum + rem
        num = num // 10
    num=sum
if num==1:
    print("magic number")
else:
    print("not magic number")
