def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    divisor_counter = 2
    while divisor_counter <= n - 2:
        if n % divisor_counter == 0:
            return False
        divisor_counter += 1

    return True