def process_list(numbers):
    new_list = numbers.copy()
    for x in numbers:
        if x < 0:
            new_list.remove(x)
    new_list.append(0)
    new_list.sort()

    return new_list
list1= [3, -1, 4, -2, 5]
result = process_list(list1)
print("Original:", list1)
print("Result:", result)