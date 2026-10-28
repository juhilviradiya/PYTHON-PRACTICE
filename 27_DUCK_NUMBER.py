num = 1020
if str(num)[0] == 0:
    print("not duck")
else:
    while num > 0:
        rem = num % 10
        if rem == 0:
            print("duck number")
            break
        num = num // 10
    else:
        print("not duck number")
        
        
        
