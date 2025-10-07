def intersection(interval1, interval2):
    def is_prime(number):
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    left = max(interval1[0], interval2[0])
    right = min(interval1[1], interval2[1])
    length = right - left

    return "YES" if length > 0 and is_prime(length) else "NO"