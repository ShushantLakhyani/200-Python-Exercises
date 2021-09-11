# Q2) Let a person input his name and his age. Print after how many years will the person be 100 years old ?
input_age = int(input("Please enteryour age:"))
input_name = input("Please enter your name:")
age_when_100 = 100 - input_age
print("His age will be 100 years after "+ str(age_when_100) +" years")
