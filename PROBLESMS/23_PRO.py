# Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
evens = []
odds = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])
    else:
        odds.append(numbers[i])
print(evens)
print(odds)
