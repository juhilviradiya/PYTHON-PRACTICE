'''
Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
'''
sentence = "Learning Python is Good!"
count = 0
for cha in sentence:
    if cha in 'AEIOUaeiou':
        count = count+1
print(f'The Total Vowels is : {count}')
    
    
