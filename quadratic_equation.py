# Q6) Write a python program to solve a quadratic equation

#SOLUTION:
#The standard form of a quadratic equation is: ax^2 + bx + c = 0, where a, b and c are real numbers and a is not equal to 0
#the solutions of a quadratic equation are given as: x = (-b +\- ((b^2-4ac)**0.5))/2a

#import the complex numbers module
import cmath

#declare any values of a,b,c
a = 1
b = 5
c = 6

#calculate the discriminant
d = (((b)**2) - (4*a*c))

#find the roots
root_1 = (-b + (d**0.5))/(2*a)
root_2 = (-b - (d**0.5))/(2*a)

#get the output of the roots
print(root_1)
print(root_2)
