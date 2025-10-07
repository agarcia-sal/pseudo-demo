def skjkasdkd(lst):
    import math

    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if num > max_prime and isPrime(num):
            max_prime = num

    result = sum(int(digit) for digit in str(max_prime))
    return result