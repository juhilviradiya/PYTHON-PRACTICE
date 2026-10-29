'''
Practice Problem: Iterate through the first 10,numbers (0–9). In each iteration,print the current number,
the previous number, and their sum.
'''
num = 10
a = 0
for i in range(num):
    c = a + i
    print(f"current number {i} previous number {a} sum : {c}")
    a = i



