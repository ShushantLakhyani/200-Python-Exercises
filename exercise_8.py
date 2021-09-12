#Q8) Write a Python program that accepts a string and calculate the number of digits and letters
#Step 1: Input a string 
input_string = input("Please enter any string: \n")
#Initialise variables to zero
a = b = 0
#in the for loops, these variables will calculate the number of letters and numbers
for a_char in input_string:
    if a_char.isdigit():
        a = a+1
    elif a_char.isalpha():
        b = b+1
    else:
        pass
#print the output
print("Letters are: ", b)
print("Digits are: ", a)
