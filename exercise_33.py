# Write a Python program to calculate the length of a string.

def string_length(str_1):
    count = 0
    for char in str_1:
        count+=1
    return count
    
print(string_length('hello world'))   
