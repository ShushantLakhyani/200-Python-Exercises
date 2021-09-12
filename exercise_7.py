# Q7)  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
#step 1: let a variable have the value 5, because of the final number of asterisks is 5
x = 5
# step 2: first 'for loop' to output the asterisks for the first 5 rows
for n in range(x):
    for j in range(n):
        print('* ',end="")
    print('')
# step 2: 'for loop' the number of asterisks for the last 4 rows
for n in range(x,0,-1):
    for j in range(n):
        print('* ',end="")
    print(' ')
