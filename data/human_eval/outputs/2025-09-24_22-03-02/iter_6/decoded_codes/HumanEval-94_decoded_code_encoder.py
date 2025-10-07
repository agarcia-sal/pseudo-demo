def skjkasdkd(lst):
    def isPrime(number):
        if number < 2:
            return False
        from math import isqrt
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    maxPrime = 0
    index = 0
    while index < len(lst):
        if lst[index] > maxPrime and isPrime(lst[index]):
            maxPrime = lst[index]
        index += 1

    digitSum = sum(int(ch) for ch in str(maxPrime))
    return digitSum