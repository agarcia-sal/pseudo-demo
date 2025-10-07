def intersection(interval1, interval2):
    def is_prime(num: int) -> bool:
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
    temp = interval2[0]
    if temp > l:
        l = temp

    r = interval1[1]
    temp = interval2[1]
    if temp < r:
        r = temp

    length = r - l

    if length > 0 and is_prime(length):
        return "YES"

    return "NO"