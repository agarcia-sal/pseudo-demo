import math

def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        limit = int(math.isqrt(n)) + 1
        for i in range(2, limit):
            if n % i == 0:
                return False
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    result = 0
    for digit_character in str(maxx):
        result += int(digit_character)
    return result