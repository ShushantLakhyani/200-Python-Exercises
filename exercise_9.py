# Count the number of even and odd numbers from a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#initialise the variables (to count the number of even and odd numbers) to zero
count_odd = 0
count_even = 0
#An if-else loop nested in a for loop to count the number of even and odd numbers
for x in numbers:
        if not x % 2:
                count_even+=1
        else:
                count_odd+=1
#print the number of even and odd numbers                
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
