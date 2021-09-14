# Q13) Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
import re
password_input = input("Please enter a password. \nThe password should contain at least one letter between [a-z].\nAtleast one lteer between [A-Z].\nAtleast one number between [0-9].\nAtleast one character amongst [$#@].\nMinimum length is 6 characters.\nMaximum length is 16 characters.\n")
if (len(password_input) < 6 or len(password_input) > 16) or not re.search("[a-z]",password_input) or not re.search("[A-Z]",password_input) or not re.search("[0-9]",password_input) or not re.search("[$#@]",password_input) or not re.search("\s",password_input):
    print("Not a valid password")
else:
    print("This password is valid")
