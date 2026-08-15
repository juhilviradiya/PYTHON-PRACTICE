num=int(input("enter the number : "))
dup=num
sum=0
power=len(str(num))
while num>0:
    rem=num%10
    sum=sum+rem**power
    power=power-1
    num=num//10
if dup==sum:
    print("disarium")
else:
    print("not disarium")
