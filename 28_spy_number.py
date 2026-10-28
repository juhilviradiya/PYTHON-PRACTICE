num = 1124
total = 0
pro = 1
while num > 0:
    rem = num % 10
    total = total + rem
    pro = pro * rem
    num = num // 10
if total == pro:
    print("spy number")
else:
    print("not spy number")
        
        
        
