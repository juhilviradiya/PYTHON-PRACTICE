'''
Practice Problem: Display only those characters which are present at an even index number in given string.
'''

S = "juhil viradiya"
for i in range(0,len(S)-1,2):
    s = S[i]
    print(s)

# we can also use slicing
S = "juhil viradiya"
ans = S[0::2]
for new in ans:
    print(new)
