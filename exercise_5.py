#Write a python program to check if a triangle is valid or not
def triangle_validity_check(a,b,c):
    if (a>b+c) or (b>a+c) or (c>a+b):
        print("This is not a valid triangle.")
    elif (a==b+c) or (b==c+a) or (c==a+b):
        print("This can form a degenerated triangle.")
    else:
        print("These values can surely form a triangle.")
        
side_1 = input("Input length of side 1:\n")
side_2 = input("Input length of side 2:\n")
side_3 = input("Input length of side 3:\n")

triangle_validity_check(side_1,side_2,side_3)
