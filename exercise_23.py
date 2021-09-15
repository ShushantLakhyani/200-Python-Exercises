# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output {40, 10, 80, 50, 20, 60, 30}

a = [10,20,30,20,10,50,60,40,80,50,40]
duplicate_items = set()
unique_items = []

for x in a:
    if x not in duplicate_items:
        unique_items.append(x)
        duplicate_items.add(x)
        
print(unique_items)
