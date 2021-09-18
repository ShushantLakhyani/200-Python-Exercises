# Q5) Write a program to find out the area of a triangle

#The semi perimeter of a triangle is: s = ((a+b+c)/2)
#The area of a triangle is: A = ((s)*(s-a)*(s-b)*(s-c))**0.5
# Here, a,b,c are the sides of the triangle

#SOLUTION:
# declare sides of the triangle
a = 5
b = 6
c = 7

#calculate the semi-perimeter
s = ((a+b+c)/2)

# calculate the area of the triangle
area = (s*(s-a)*(s-b)*(s-c))**0.5

#output the area of the triangle
print(area)
