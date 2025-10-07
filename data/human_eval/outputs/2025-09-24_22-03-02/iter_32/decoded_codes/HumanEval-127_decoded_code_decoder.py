def intersection(interval1, interval2):
    def is_prime(num: int) -> bool:
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        i = 2
        while i < num:
            if num % i == 0:
                return False
            i += 1
        return True

    l = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    r = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    length = r - l
    if length > 0:
        result_prime = is_prime(length)
        if result_prime:
            return "YES"
    return "NO"