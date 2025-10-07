def intersection(interval1, interval2):
    def is_prime(num):
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    left_endpoint = max(interval1[0], interval2[0])
    right_endpoint = min(interval1[1], interval2[1])
    length = right_endpoint - left_endpoint

    if length > 0 and is_prime(length):
        return "YES"
    else:
        return "NO"