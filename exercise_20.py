# Write a Python program to get the largest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2
def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
