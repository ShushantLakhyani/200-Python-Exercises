# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

color_1 = ['Red','Green','Orange','White']
color_2 = ['Black','Green','White','Pink']
print ((set(color_1)) & (set(color_2)))            
