num=int(input("enter the number :"))
dup=num
sum=0
while num >0:
    rem=num%10
    fact = 1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if sum==dup:
    print("peterson")
else:
    print("not peterson")
