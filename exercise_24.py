# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

def second_smallest_number(numbers):
    a1,a2 = float('inf'),float('inf')
    for x in numbers:
        if x <=a1:
            a1,a2 = x,a1
        elif x<a2:
            a2 = x
    return a2
second_smallest_number([1, 2, -8, -2, 0])
