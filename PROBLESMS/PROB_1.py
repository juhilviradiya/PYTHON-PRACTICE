'''
Practice Problem: Write a Python function that accepts two integer numbers.
If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
'''

def number(num1,num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
result = number(20,30)
print("The Result is : ",result)

result=(number(40,60))
print("The Result is : ",result)
