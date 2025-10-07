def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def intersection(i1, i2):
    l = max(i1[0], i2[0])
    r = min(i1[1], i2[1])
    length = r - l
    return "YES" if length > 0 and is_prime(length) else "NO"