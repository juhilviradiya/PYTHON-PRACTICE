def composite():
    if num > 0:
        for i in range(2,num//2+1):
            if num % i == 0:
                  return "composite"
        else:
            return "not composite"
    return "not composite"
num=8
print(composite())
