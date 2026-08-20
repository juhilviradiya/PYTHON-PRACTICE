def prime():
    if num > 0:
        for i in range(2,num//2+1):
            if num % i == 0:
                return "not prime"
        return "prime"
    return "not prime"
