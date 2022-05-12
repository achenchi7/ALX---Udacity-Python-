##check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
for prime in check_prime:
    for i in range (2, prime):
        if (prime % i)== 0:
            print("{} is NOT a prime number because {} is a factor of {}".format(prime, i, prime))
            break
        
        if i == prime -1:
            print("{} is a prime number".format(prime))