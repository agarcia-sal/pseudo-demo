def skjkasdkd(lst):
    def isPrime(n):
        i = 2
        while i <= int(pow(n, 0.5)) + 1:
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
    index = 0
    str_maxx = str(maxx)
    while index < len(str_maxx):
        char = str_maxx[index]
        digit = int(char)
        result += digit
        index += 1

    return result