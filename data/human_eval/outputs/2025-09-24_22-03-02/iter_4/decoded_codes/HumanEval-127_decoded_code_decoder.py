def intersection(interval1, interval2):
    def is_prime(number):
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    left = max(interval1[0], interval2[0])
    right = min(interval1[1], interval2[1])
    length = right - left
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"