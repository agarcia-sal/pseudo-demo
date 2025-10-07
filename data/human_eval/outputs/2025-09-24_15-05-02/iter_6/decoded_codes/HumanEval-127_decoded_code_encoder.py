def intersection(interval1, interval2):
    def is_prime(number):
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    left_endpoint = max(interval1[0], interval2[0])
    right_endpoint = min(interval1[1], interval2[1])
    intersection_length = right_endpoint - left_endpoint

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    return "NO"