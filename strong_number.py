def fact(num):
    result = 1
    while num > 0:
        result= num * result
        num-=1
    return result
def strong(num):
    dup = num
    total = 0
    while num > 0:
        rem = num % 10
        total = total + fact(rem)
        num = num // 10
    if  dup == total:
        return 'STRONG NUMBER'
    return 'NOT STRONG NUMBER' 
num = 145
print(strong(num))   
