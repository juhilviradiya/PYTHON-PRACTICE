num=int(input("enter the number :"))
dup=num
sum=0
while num >0:
    rem=num%10
    sum=sum+rem
    num=num//10
if dup%sum==0:
    print("harshad")
else:
    print("not harshad")
