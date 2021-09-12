#Write a python program to generate the fibonacci series between 0 and 50
#Fibonacci series: The Fibonacci numbers are the numbers in the following integer sequence :0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
#The general formula for Fibonacci Series is: F(n) = F(n-1) + F(n-2)
#Initialise the value of first two variables as 0 and 1
a,b = 0,1
#Print a as the initial value in the fibonacci series is zero
print(a)
#Have a for loop to get the further values. The first statement states b<50 because we want to evaluate for values less than 50
while b < 50:
    #This statement would print the current value for b
    print(b)
    #This statement would assign the current value of b to a, and would assign the current value of b+a  to b
    a,b = b,a+b
