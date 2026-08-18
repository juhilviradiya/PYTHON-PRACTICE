num1=int(input("enter the number : "))
num2=int(input("enter the number :")) 
count1=0
for i in range(1,num1//2+1):
    if num1 % i == 0:
        count1+=1
count2=0
for i in range(1,num2//2+1):
    if num2 % i == 0:
        count2+=1
if count1==1 and count2==1 and abs(num1-num2)==2:
    print("twin prime number ")
else:
    print("not twin prime number")
