import math       #找出100以内素数

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(2,100) if is_prime(i)]
print(primes)
