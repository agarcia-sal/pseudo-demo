from math import isqrt

def skjkasdkd(lst: list[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    maxx = 0
    for i in range(len(lst)):
        val = lst[i]
        if val > maxx and isPrime(val):
            maxx = val

    result = 0
    str_maxx = str(maxx)
    for digit_char in str_maxx:
        result += int(digit_char)

    return result