#  Write a Python program to change a given string to a new string where the first and last chars have been exchanged
def change_string(str_1):
    return str_1[-1:] + str_1[1:-1] + str_1[:1]

print(change_string('abcd'))
print(change_string('12345'))
