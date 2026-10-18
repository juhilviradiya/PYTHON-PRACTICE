def prime(num):
    if num <= 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return True
    return False
        
def reverse(num):
    ans = 0
    while num > 0:
        ans = 0
        rem = num % 10
        ans = ans*10 + rem
        num = num // 10
    return ans
def emirp(num):
    rev = reverse(num)
    if prime(num) == prime(rev) and num != rev: 
        return 'EMIRP'
    return 'NOR EMIRP'
num = 13
var = emirp(num)
print(var)
    
