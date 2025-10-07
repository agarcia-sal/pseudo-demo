def skjkasdkd(lst):
    import math

    def isPrime(n):
        if n < 2:
            return False
        i = 2
        while i <= int(pow(n, 0.5) + 1):
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]) == True:
            maxx = lst[i]
        i += 1

    result = 0
    str_maxx = str(maxx)
    j = 0
    while j < len(str_maxx):
        character = str_maxx[j]
        integer_digit = int(character)
        result += integer_digit
        j += 1

    return result