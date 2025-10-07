def intersection(interval1, interval2):
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        i = 2
        while i < num:
            if num % i == 0:
                return False
            i += 1
        return True

    l = interval1[0]
    if interval2[0] > l:
        l = interval2[0]

    r = interval1[1]
    if interval2[1] < r:
        r = interval2[1]

    length = r - l

    if length > 0 and is_prime(length):
        return "YES"

    return "NO"