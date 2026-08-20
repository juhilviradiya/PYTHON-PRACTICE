def neon():
    if num > 0:
        sum=0
        dup=num
        sqare=num*num
        while sqare > 0:
            rem=sqare % 10
            sum = sum + rem
            sqare=sqare // 10
        if dup == sum:
            return "neon"
        else:
            return "not neon"
    return "not neon"
num=9
print(neon())
