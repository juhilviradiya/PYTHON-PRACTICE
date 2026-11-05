#Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for ans in words:
    length = len(ans)
    print(f'{ans} - {length}')
