import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def PrimeList(N):
    primes = []
    for num in range(2, N):
        if is_prime(num):
            primes.append(str(num))
    return ' '.join(primes)
