# Write a Python program to check whether an alphabet is a vowel or consonant
alphabet_input = input("Please enter any alphabet").lower()
if alphabet_input in ['a','e','i','o','u']:
    print("It is a vowel")
else:
    print("It is a consonant")
