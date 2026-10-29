'''
Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first
list and even numbers from the second list.
'''
def merge_list(list1,list2):
    num = []
    for L1 in list1:
        if L1 % 2 != 0:
            num.append(L1)
           

    for L2 in list2:
        if L2 % 2 == 0:
            num.append(L2)
            
    return num
        
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(merge_list(list1,list2))
