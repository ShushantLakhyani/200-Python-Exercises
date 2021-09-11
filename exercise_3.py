#Q3) Input a number n, between 1-9. Then, the output should give the result as: n + nn + nnn
input_int = int(input("Enter any integer between 1-9:"))
input_int_10 = (input_int*10) + (input_int)
input_int_100 = (input_int*100) + (input_int*10) + (input_int*1)
print(input_int+input_int_10+input_int_100)
