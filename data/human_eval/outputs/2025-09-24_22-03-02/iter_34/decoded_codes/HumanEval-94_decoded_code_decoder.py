import math

def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        limit = int(math.isqrt(n)) + 1
        i = 2
        while i < limit:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    maxx_str = str(maxx)
    sum_digits = 0
    j = 0
    while j < len(maxx_str):
        digit_int = int(maxx_str[j])
        sum_digits += digit_int
        j += 1

    return sum_digits