def perfect():
    if num > 0:
        dup=num
        sum=0
        for i in range(1,num):
            if num % i == 0:
                sum=sum+i
        if dup == sum:
            return "perfect"
        else:
            return "not perfect" 
    return "not perfect"       
num=5
print(perfect())
