num=int(input("enter the numebr : "))
sqr=num * num
if sqr % (10**len(str(num)))==num:
    print("automorphic")
else:
    print("not automorphic")
