from math import sqrt

def intersection(interval1, interval2):
    def is_prime(number):
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        limit = int(sqrt(number)) + 1
        for i in range(3, limit, 2):
            if number % i == 0:
                return False
        return True

    left_bound = max(interval1[0], interval2[0])
    right_bound = min(interval1[1], interval2[1])
    length = right_bound - left_bound

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"