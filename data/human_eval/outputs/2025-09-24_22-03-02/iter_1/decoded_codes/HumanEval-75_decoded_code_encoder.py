def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def is_multiply_prime(a):
    for i in range(2, 101):
        if is_prime(i):
            for j in range(2, 101):
                if is_prime(j):
                    for k in range(2, 101):
                        if is_prime(k):
                            if i * j * k == a:
                                return True
    return False