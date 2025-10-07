def is_prime(n: int) -> bool:
    temp_val = 2
    if n < 2:
        return False

    while temp_val <= n - 2:
        rem = n % temp_val
        if rem == 0:
            return False
        temp_val += 1

    return True