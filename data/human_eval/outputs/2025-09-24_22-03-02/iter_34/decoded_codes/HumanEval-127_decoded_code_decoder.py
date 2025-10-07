def intersection(interval1, interval2):
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        i = 2
        while i < num:
            remainder = num - (num // i) * i
            if remainder == 0:
                return False
            i += 1
        return True

    l = interval1[0]
    m = interval2[0]
    if m > l:
        l = m

    r = interval1[1]
    n = interval2[1]
    if n < r:
        r = n

    length = r - l

    if length > 0:
        prime_check = is_prime(length)
        if prime_check:
            return "YES"

    return "NO"