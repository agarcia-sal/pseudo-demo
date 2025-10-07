def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    maxx = 0
    for val in lst:
        if val > maxx and isPrime(val):
            maxx = val

    return sum(int(d) for d in str(maxx))