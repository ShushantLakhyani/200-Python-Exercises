# Q7) Write a python program to swap 2 variables

#Method 1: Using a temporary variable

#Solution:

#Decalre two variables with two values

a = 1
b = 2

#create a temporary variable to swap the values, and swap the values in the following way:
# assign the value of 'a' to the temporary variable
temp = a

#assign the value of 'b' to 'a'
a = b

#assign the value of temp to 'b'
b = temp

#get the output
print(a)
print(b)

#Method 2: withoout using temporaryh variable

# Swap the values as illustrated below
a, b = b, a

#get the output
print(a)
print(b)


#Method 3: By additions and substractions
a = a + b
b = a - b
a = a - b

#get the output
print(a)
print(b)

#Method 4: By multiplication and division
a = a * b
b = a/b
a = a/b

#get the output
print(a)
print(b)

#Method 5: By XOR
a = int(a)
b = int(b)
a = a ^ b
b = a ^ b
a = a ^ b

#get the output
print(a)
print(b)
