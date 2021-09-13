# Q11)  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
a = []
for n in range(1500,2700):
    if n%7==0 and n%5==0:
        a.append(str(n))
        
print(','.join(a))
