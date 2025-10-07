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

    left_bound = max(interval1[0], interval2[0])
    right_bound = min(interval1[1], interval2[1])
    intersection_length = right_bound - left_bound

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    return "NO"