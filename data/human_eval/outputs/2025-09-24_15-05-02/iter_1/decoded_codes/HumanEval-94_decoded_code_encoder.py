def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_max_prime_digits(lst):
    maxp = max((x for x in lst if isPrime(x)), default=0)
    return sum(int(digit) for digit in str(maxp))