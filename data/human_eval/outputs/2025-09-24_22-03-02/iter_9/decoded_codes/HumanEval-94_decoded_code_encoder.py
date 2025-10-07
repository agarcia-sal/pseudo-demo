def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    for num in lst:
        if num > maxx and isPrime(num):
            maxx = num

    return sum(int(d) for d in str(maxx))