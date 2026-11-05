def exponent(base, exp):
    num = exp
    result = 1
    # Repeat multiplication 'exp' times
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is:", result)

exponent(2, 5)
