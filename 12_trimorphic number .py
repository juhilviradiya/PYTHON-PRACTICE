num=int(input("enter the number : "))
cube=num**3
digits=len(str(num))
divisor=10**digits
if cube % divisor==num:
    print("trimorphic number ")
else:
    print("not trimorphic number ")
