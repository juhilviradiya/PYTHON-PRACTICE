num=int(input("enter the number : "))
dup=num
while num > 9:
    sum=0
    while num >0:
        rem=num%10
        sum=sum+rem**2
        num=num//10
    num=sum
if num==1 or num==7:
    print("happy")
else:
    print("not happy")
