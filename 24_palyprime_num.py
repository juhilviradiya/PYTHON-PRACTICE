def palimdrome(num):
    dup = num
    total = 0
    while num > 0:
        rem = num % 10
        total = total*10 + rem
        num = num // 10
    if dup == total:
        return True
    return False
    
def prime(num):
    num = palimdrome(num)
    if num <= 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

        
def palyprime(num):
    if palimdrome(num) == prime(num):
        return 'palyprime'
    return "not palyprime"   
num = 131
var = palyprime(num)
print(var)         
