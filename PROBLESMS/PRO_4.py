'''
Practice Problem: Write a function to remove characters from a string starting
from index 0 up to n and return a new string.
'''
def remove_char(word,num):
    ans = word[num:]
    return ans

print(remove_char('America',2))
print(remove_char('patel',1))
