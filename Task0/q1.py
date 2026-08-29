n=int(input("Enter number of elements: "))
a=[]
for i in range(n): 
    x = int(input("Enter elements: ")) 
    a.append(x)
largest = a[0]
smallest = a[0]
total = 0
even = 0
odd = 0

for num in a:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    total=total+num
print("Largest:", largest) 
print("Smallest:", smallest) 
print("Sum:", total) 
print("Even count:", even) 
print("Odd count:", odd) 
print("Reversed:", a[::-1])
