def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def intersection(a, b):
    l = max(a[0], b[0])
    r = min(a[1], b[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    else:
        return "NO"