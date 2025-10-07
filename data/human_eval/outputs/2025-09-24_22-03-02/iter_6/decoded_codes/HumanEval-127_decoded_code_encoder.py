def intersection(interval1, interval2):
    def is_prime(number):
        if number in (0, 1):
            return False
        if number == 2:
            return True
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    left_bound = max(interval1.start, interval2.start)
    right_bound = min(interval1.end, interval2.end)
    intersection_length = right_bound - left_bound

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    return "NO"