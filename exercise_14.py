# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

length_1 = int(input("Please enter length of side 1\n"))
length_2 = int(input("Please enter length of side 2\n"))
length_3 = int(input("Please enter length of side 3\n"))

if length_1 == length_2 and length_2 == length_3  and length_3 == length_1:
    print("The triangle is equilateral.")
    
elif length_1 == length_2 or length_2 == length_3  or length_3 == length_1:
    print("It is an isosceles triangle")
    
else:
    print("It is a scalene triangle")
