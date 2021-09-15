# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]
list_1 = [1,2,3,4]
list_2 = [1,2]
print(list(set(list_1) - set(list_2)) )
