def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    else:
        #The else block executes when the for loop completes without a break statement.
        return True
    
n = int(input("Enter number: "))
for number in range(2, n + 1):
    if is_prime(number):
        print(number, end=" ")