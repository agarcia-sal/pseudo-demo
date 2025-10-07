def skjkasdkd(lst) -> int:
    def isPrime(n: int) -> bool:
        limit = int(n ** 0.5) + 1
        i = 2
        while i < limit:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]) is True:
            maxx = lst[i]
        i += 1

    result = 0
    j = 0
    str_maxx = str(maxx)
    while j < len(str_maxx):
        digit_char = str_maxx[j]
        digit_int = int(digit_char)
        result += digit_int
        j += 1

    return result