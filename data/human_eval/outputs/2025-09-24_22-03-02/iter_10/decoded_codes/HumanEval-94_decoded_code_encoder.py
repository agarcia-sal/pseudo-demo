def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        i = 2
        limit = int(n ** 0.5) + 1
        while i <= limit:
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

    result = 0
    for digit in str(maxx):
        result += int(digit)
    return result