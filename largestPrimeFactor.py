import math
def largest_prime(n):
    primes = []
    while n%2 == 0:
        primes.append(2)
        n = n/2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            primes.append(i)
            n = n/i
    
    return max(primes)




