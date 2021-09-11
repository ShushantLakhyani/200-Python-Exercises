#Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
num_rows = int(input("Input number of rows: "))
num_cols = int(input("Number of columns: "))

new_list = [[0 for col in range(num_cols)] for row in range(num_rows)]
for row in range(num_rows):
    for col in range(num_cols):
        new_list[row][col] = row*col
        
print(new_list)
