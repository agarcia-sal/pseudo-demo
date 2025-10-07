def intersection(interval1, interval2) -> str:
    def is_prime(num: int) -> bool:
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0:
        if is_prime(length):
            return "YES"
    return "NO"