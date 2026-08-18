num=int(input("enter the number :"))
sqare=num**2
digits=len(str(num))
divisor=10**digits
right=sqare % divisor
left=sqare // divisor
if right + left == num:
    print("kaprekar number ")
else:
    print("not kaprekar number")
